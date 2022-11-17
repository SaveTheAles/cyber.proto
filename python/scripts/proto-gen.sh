#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

echo "install betterproto... pre-release for now. stable one has some issues"
#pip install --upgrade "avast.betterproto[compiler]"
pip install --upgrade "betterproto[compiler]" --pre

OUT_DIR="./cyber_proto"

mkdir -p "$OUT_DIR"

echo "Processing go-cyber, terrad and liquidity proto files ..."

TERRAD_DIR="../terrad/proto"
TERRAD_THIRD_PARTY_DIR="../terrad/third_party/proto"
CYBER_DIR="../go-cyber/proto"
CYBER_THIRD_PARTY_DIR="../go-cyber/third_party/proto"
LIQUIDITY_DIR="../liquidity/proto"
LIQUIDITY_THIRD_PARTY_DIR="../liquidity/third_party/proto"

protoc \
  --proto_path=${TERRAD_DIR} \
  --proto_path=${TERRAD_THIRD_PARTY_DIR} \
  --python_betterproto_out="${OUT_DIR}" \
  $(find ${TERRAD_DIR} ${TERRAD_THIRD_PARTY_DIR}  -path -prune -o -name '*.proto' -print0 | xargs -0)

protoc \
  --proto_path=${LIQUIDITY_DIR} \
  --proto_path=${LIQUIDITY_THIRD_PARTY_DIR} \
  --python_betterproto_out="${OUT_DIR}" \
  $(find ${LIQUIDITY_THIRD_PARTY_DIR} ${LIQUIDITY_DIR}  -path -prune -o -name '*.proto' -print0 | xargs -0)

protoc \
  --proto_path=${CYBER_DIR} \
  --proto_path=${CYBER_THIRD_PARTY_DIR} \
  --python_betterproto_out="${OUT_DIR}" \
  $(find ${CYBER_DIR} ${CYBER_THIRD_PARTY_DIR}  -path -prune -o -name '*.proto' -print0 | xargs -0)