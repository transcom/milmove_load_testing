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
      rev = "0093e4e6a9998f1ff59e79ec31f2341770b7bebb";
    }) {}).editorconfig-core-c

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "python3-3.9.6";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "2f216e02f453cf64cb3b06c1e564ea53bdc01fa0";
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
      name = "shellcheck-0.7.2";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "7cf6cbe49a4f9efa0607437447d256bbd206b0c4";
    }) {}).shellcheck

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "aws-vault-6.3.1";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "3453b89f4bba270e2d82f6248b09b9595bb47f4b";
    }) {}).aws-vault

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "awscli2-2.2.14";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "b3519ced7d0de81573ee0f0874657c76f2d944b5";
    }) {}).awscli2

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "chamber-2.10.2";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "e63d487cd80754ca9ce18d66fa09e0bcb7dce3f7";
    }) {}).chamber

    (import (builtins.fetchGit {
      # Descriptive name to make the store path easier to identify
      name = "jq-1.6";
      url = "https://github.com/NixOS/nixpkgs/";
      ref = "refs/heads/nixpkgs-unstable";
      rev = "0093e4e6a9998f1ff59e79ec31f2341770b7bebb";
    }) {}).jq

];
}
