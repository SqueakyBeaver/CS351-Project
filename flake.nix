{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = {
    self,
    nixpkgs,
  }: let
    supportedSystems = ["x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin"];
    forEachSupportedSystem = f:
      nixpkgs.lib.genAttrs supportedSystems (system:
        f {
          pkgs = import nixpkgs {inherit system;};
        });

    /*
    * Change this value ({major}.{min}) to
    * update the Python virtual-environment
    * version. When you do this, make sure
    * to delete the `.venv` directory to
    * have the hook rebuild it for the new
    * version, since it won't overwrite an
    * existing one. After this, reload the
    * development shell to rebuild it.
    * You'll see a warning asking you to
    * do this when version mismatches are
    * present. For safety, removal should
    * be a manual step, even if trivial.
    */
    version = "3.12";
  in {
    devShells = forEachSupportedSystem ({pkgs}: let
      concatMajorMinor = v:
        pkgs.lib.pipe v [
          pkgs.lib.versions.splitVersion
          (pkgs.lib.sublist 0 2)
          pkgs.lib.concatStrings
        ];

      python = pkgs."python${concatMajorMinor version}";
      venvDir = ".venv";
    in {
      default = pkgs.mkShell {
        shellHook = ''
          SOURCE_DATE_EPOCH=$(date +%s)

          if [ -d "${venvDir}" ]; then
            echo "Skipping venv creation, '${venvDir}' already exists"
          else
            echo "Creating new venv environment in path: '${venvDir}'"
            # Note that the module venv was only introduced in python 3, so for 2.7
            # this needs to be replaced with a call to virtualenv
            ${python.interpreter} -m venv "${venvDir}" --copies --system-site-packages
          fi

          # Under some circumstances it might be necessary to add your virtual
          # environment to PYTHONPATH, which you can do here too;

          source "${venvDir}/bin/activate"

          runHook postShellHook
        '';

        postShellHook = ''
          venvVersionWarn() {
          	local venvVersion
          	venvVersion="$("${venvDir}/bin/python" -c 'import platform; print(platform.python_version())')"

          	[[ "$venvVersion" == "${python.version}" ]] && return

          	cat <<EOF
          Warning: Python version mismatch: [$venvVersion (venv)] != [${python.version}]
                       Delete '$venvDir' and reload to rebuild for version ${python.version}
          EOF
          }

          venvVersionWarn

          # Fucky bash script to patch this son of a bitch
          # God I hate and love NixOS
          VENV_PYTHON="$PWD/${venvDir}/bin/python"
          ORIG_PYTHON="$VENV_PYTHON.orig"

          if [[ -f "$VENV_PYTHON" && ! -f "$ORIG_PYTHON" ]]; then
            echo "[nix-ld patch] Wrapping .venv/bin/python with LD_LIBRARY_PATH"

            mv "$VENV_PYTHON" "$ORIG_PYTHON"

            cat > "$VENV_PYTHON" <<EOF
          #!/usr/bin/env bash
          export LD_LIBRARY_PATH=${pkgs.lib.escapeShellArg "$NIX_LD_LIBRARY_PATH"}
          exec "$ORIG_PYTHON" "\$@"
          EOF

            chmod +x "$VENV_PYTHON"
          else
            echo "[nix-ld patch] Wrapper already applied or missing .venv/bin/python"
          fi

        '';

        PYTHONPATH = pkgs.runCommand "pythonpath" {} ''
          echo $PWD/${venvDir}/${python.sitePackages}/:$PYTHONPATH > $out
        '';

        NIX_LD_LIBRARY_PATH = with pkgs;
          lib.makeLibraryPath [
            glib
            libGL
            nss
            fontconfig
            nspr
            dbus
            zlib
            zstd
            stdenv.cc.cc
            libsodium
            libxkbcommon
            freetype
            xcb-util-cursor
            xorg.libX11
            xorg.libxcb
            xorg.xcbutilwm
            xorg.xcbutilimage
            xorg.xcbutilkeysyms
            xorg.xcbutil
            xorg.xcbutilrenderutil
          ];

        # https://github.com/nix-community/nix-ld/issues/19
        NIX_LD = pkgs.runCommand "ld.so" {} ''
          ln -s "$(cat '${pkgs.stdenv.cc}/nix-support/dynamic-linker')" $out
        '';

        packages = [
          (
            python.withPackages
            (ps:
              with ps; [
                pip
                mysql-connector
                tkinter
              ])
            )
            pkgs."python${concatMajorMinor version}Packages".tkinter
        ];
      };
    });
  };
}
