#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

echo "install betterproto... pre-release for now. stable one has some issues"
#pip install --upgrade "avast.betterproto[compiler]"
pip install --upgrade "betterproto[compiler]" --pre

OUT_DIR="./cyber_proto"

mkdir -p "$OUT_DIR"

echo "Processing terrad and go-cyber proto files ..."

TERRAD_DIR="../terrad/proto"
TERRAD_THIRD_PARTY_DIR="../terrad/third_party/proto"
CYBER_DIR="../go-cyber/proto"

protoc \
  --proto_path=${TERRAD_DIR} \
  --proto_path=${TERRAD_THIRD_PARTY_DIR} \
  --proto_path=${CYBER_DIR} \
  --python_betterproto_out="${OUT_DIR}" \
  $(find ${TERRAD_DIR} ${TERRAD_THIRD_PARTY_DIR} ${CYBER_DIR} -path -prune -o -name '*.proto' -print0 | xargs -0)
