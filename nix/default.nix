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
      name = "python3-3.10.11";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "0b6445b611472740f02eae9015150c07c5373340";
    }) {}).python310Full

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "pipenv-2023.2.4";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "0b6445b611472740f02eae9015150c07c5373340";
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

    (import
      (builtins.fetchGit {
        # Descriptive name to make the store path easier to identify
        name = "circleci-cli-0.1.15663";
        url = "https://github.com/NixOS/nixpkgs/";
        ref = "refs/heads/nixpkgs-unstable";
        rev = "23cedc3088a628e1f5454cab6864f9b1a059e1ba";
      })
      { }).circleci-cli

  ];

  # the pre-commit hooks expects the binary to be `circleci`
  postBuild = ''
  ln -s $out/bin/circleci-cli $out/bin/circleci
  '';
}
