# use ./nix/update.sh to install
#
# use https://ahobson.github.io/nix-package-search/#/search to find rev for specific package version

let
  pkgs = import <nixpkgs> {};
  inherit (pkgs) buildEnv;
in buildEnv {
  name = "milmove-load-testing-packages";
  paths = [

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "editorconfig-core-c-0.12.1";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "c8ff5bc6f74a2960fab5ae417cd2bb055eab1002";
    }) {}).editorconfig-core-c

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "python3-3.9.9";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "3fdeef8a7ee81787a099cfb57bd91f24c5ec587d";
    }) {}).python39Full

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "pipenv-2021.5.29";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "fe296b79b4c803fec51410a987a11f077715a845";
    }) {}).pipenv

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "shellcheck-0.8.0";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "de5ab3881e4868dcfa9f75723bd035ce99cb0751";
    }) {}).shellcheck

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "aws-vault-6.4.0";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "8bd55a6a5ab05942af769c2aa2494044bff7f625";
    }) {}).aws-vault

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "awscli2-2.2.40";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "6f0b0bb7028cf612298673bf6b5d453bcc7af965";
    }) {}).awscli2

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "chamber-2.10.7";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "3fdeef8a7ee81787a099cfb57bd91f24c5ec587d";
    }) {}).chamber

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "jq-1.6";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "725ef07e543a6f60b534036c684d44e57bb8d5de";
    }) {}).jq

];
}
