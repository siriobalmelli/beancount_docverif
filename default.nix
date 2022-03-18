{
  nixpkgs ? import (builtins.fetchGit {
    url = "https://siriobalmelli@github.com/siriobalmelli-foss/nixpkgs.git";
    ref = "master";
    }) {}
}:

with nixpkgs;
with nixpkgs.python3.pkgs;

buildPythonPackage rec {
  pname = "beancount_docverif";
  version = "1.0.1";
  disabled = !isPy3k;

  src = ./.;

  leaveDotGit = true;
  nativeBuildInputs = [
    git
    setuptools_scm
    twine
  ];
  propagatedBuildInputs = [
    beancount
  ];

  checkInputs = [
    beancount
    pytest
  ];
  checkPhase = ''
    pytest
  '';
}
