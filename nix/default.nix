# to install
# nix-env -f nix -i
#
# use
#
# https://ahobson.github.io/nix-package-search/#/search
#
# to find rev for specific package version

let
  pkgs = import <nixpkgs> {};
  inherit (pkgs) buildEnv;
in buildEnv {
  name = "milmove-load-testing-packages";
  paths = [

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "python3-3.8.8";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "89dacdd7a518c14d3e824d4c6cc0cc93002367f6";
    }) {}).python3

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "pre-commit-2.7.1";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "559cf76fa3642106d9f23c9e845baf4d354be682";
    }) {}).pre-commit

];
}
