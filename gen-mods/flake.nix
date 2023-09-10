{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in
      {
        packages.default = pkgs.runCommand "pybazelproto-gen-mods"
          {
            buildInputs = [
              pkgs.protobuf
            ];
            bazel = pkgs.fetchFromGitHub {
              owner = "bazelbuild";
              repo = "bazel";
              rev = "abac1c632ef0f2c2fac8858abf9b6f9657cb19c2";
              hash = "sha256-AaiCytSWg1g/JDgivrl2dgQaUPT+LbBJ13kQ3+N1kYc=";
            };
          } ''
          protoc -I=$bazel --python_out=. $bazel/src/main/protobuf/build.proto $bazel/src/main/protobuf/analysis_v2.proto
          sed -i 's/from src.main.protobuf import build_pb2/from . import build_pb2/g' ./src/main/protobuf/analysis_v2_pb2.py
          mkdir $out
          cp ./src/main/protobuf/* $out/
        '';
      }
    );
}
