# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cyber/bandwidth/v1beta1/genesis.proto, cyber/bandwidth/v1beta1/query.proto, cyber/bandwidth/v1beta1/types.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    recovery_period: int = betterproto.uint64_field(1)
    adjust_price_period: int = betterproto.uint64_field(2)
    base_price: str = betterproto.string_field(3)
    base_load: str = betterproto.string_field(4)
    max_block_bandwidth: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class NeuronBandwidth(betterproto.Message):
    neuron: str = betterproto.string_field(1)
    remained_value: int = betterproto.uint64_field(2)
    last_updated_block: int = betterproto.uint64_field(3)
    max_value: int = betterproto.uint64_field(4)


@dataclass(eq=False, repr=False)
class Price(betterproto.Message):
    price: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryLoadRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryLoadResponse(betterproto.Message):
    load: "___cosmos_base_v1_beta1__.DecProto" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryPriceRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryPriceResponse(betterproto.Message):
    price: "___cosmos_base_v1_beta1__.DecProto" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalBandwidthRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryTotalBandwidthResponse(betterproto.Message):
    total_bandwidth: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryNeuronBandwidthRequest(betterproto.Message):
    neuron: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryNeuronBandwidthResponse(betterproto.Message):
    neuron_bandwidth: "NeuronBandwidth" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    params: "Params" = betterproto.message_field(1)


class QueryStub(betterproto.ServiceStub):
    async def load(self) -> "QueryLoadResponse":

        request = QueryLoadRequest()

        return await self._unary_unary(
            "/cyber.bandwidth.v1beta1.Query/Load", request, QueryLoadResponse
        )

    async def price(self) -> "QueryPriceResponse":

        request = QueryPriceRequest()

        return await self._unary_unary(
            "/cyber.bandwidth.v1beta1.Query/Price", request, QueryPriceResponse
        )

    async def total_bandwidth(self) -> "QueryTotalBandwidthResponse":

        request = QueryTotalBandwidthRequest()

        return await self._unary_unary(
            "/cyber.bandwidth.v1beta1.Query/TotalBandwidth",
            request,
            QueryTotalBandwidthResponse,
        )

    async def neuron_bandwidth(
        self, *, neuron: str = ""
    ) -> "QueryNeuronBandwidthResponse":

        request = QueryNeuronBandwidthRequest()
        request.neuron = neuron

        return await self._unary_unary(
            "/cyber.bandwidth.v1beta1.Query/NeuronBandwidth",
            request,
            QueryNeuronBandwidthResponse,
        )

    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/cyber.bandwidth.v1beta1.Query/Params", request, QueryParamsResponse
        )


class QueryBase(ServiceBase):
    async def load(self) -> "QueryLoadResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def price(self) -> "QueryPriceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_bandwidth(self) -> "QueryTotalBandwidthResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def neuron_bandwidth(self, neuron: str) -> "QueryNeuronBandwidthResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_load(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.load(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_price(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.price(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_total_bandwidth(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.total_bandwidth(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_neuron_bandwidth(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "neuron": request.neuron,
        }

        response = await self.neuron_bandwidth(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cyber.bandwidth.v1beta1.Query/Load": grpclib.const.Handler(
                self.__rpc_load,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryLoadRequest,
                QueryLoadResponse,
            ),
            "/cyber.bandwidth.v1beta1.Query/Price": grpclib.const.Handler(
                self.__rpc_price,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryPriceRequest,
                QueryPriceResponse,
            ),
            "/cyber.bandwidth.v1beta1.Query/TotalBandwidth": grpclib.const.Handler(
                self.__rpc_total_bandwidth,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalBandwidthRequest,
                QueryTotalBandwidthResponse,
            ),
            "/cyber.bandwidth.v1beta1.Query/NeuronBandwidth": grpclib.const.Handler(
                self.__rpc_neuron_bandwidth,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryNeuronBandwidthRequest,
                QueryNeuronBandwidthResponse,
            ),
            "/cyber.bandwidth.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }


from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
