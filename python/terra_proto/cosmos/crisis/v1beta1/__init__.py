# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crisis/v1beta1/genesis.proto, cosmos/crisis/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class MsgVerifyInvariant(betterproto.Message):
    """
    MsgVerifyInvariant represents a message to verify a particular invariance.
    """

    sender: str = betterproto.string_field(1)
    invariant_module_name: str = betterproto.string_field(2)
    invariant_route: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgVerifyInvariantResponse(betterproto.Message):
    """
    MsgVerifyInvariantResponse defines the Msg/VerifyInvariant response type.
    """

    pass


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the crisis module's genesis state."""

    # constant_fee is the fee used to verify the invariant in the crisis module.
    constant_fee: "__base_v1_beta1__.Coin" = betterproto.message_field(3)


class MsgStub(betterproto.ServiceStub):
    async def verify_invariant(
        self,
        *,
        sender: str = "",
        invariant_module_name: str = "",
        invariant_route: str = ""
    ) -> "MsgVerifyInvariantResponse":

        request = MsgVerifyInvariant()
        request.sender = sender
        request.invariant_module_name = invariant_module_name
        request.invariant_route = invariant_route

        return await self._unary_unary(
            "/cosmos.crisis.v1beta1.Msg/VerifyInvariant",
            request,
            MsgVerifyInvariantResponse,
        )


class MsgBase(ServiceBase):
    async def verify_invariant(
        self, sender: str, invariant_module_name: str, invariant_route: str
    ) -> "MsgVerifyInvariantResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_verify_invariant(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "sender": request.sender,
            "invariant_module_name": request.invariant_module_name,
            "invariant_route": request.invariant_route,
        }

        response = await self.verify_invariant(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.crisis.v1beta1.Msg/VerifyInvariant": grpclib.const.Handler(
                self.__rpc_verify_invariant,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgVerifyInvariant,
                MsgVerifyInvariantResponse,
            ),
        }


from ...base import v1beta1 as __base_v1_beta1__
