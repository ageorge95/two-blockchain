from dataclasses import dataclass
from typing import Optional

from two.types.blockchain_format.sized_bytes import bytes32
from two.types.blockchain_format.vdf import VDFInfo, VDFProof
from two.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class SignagePoint(Streamable):
    cc_vdf: Optional[VDFInfo]
    cc_proof: Optional[VDFProof]
    rc_vdf: Optional[VDFInfo]
    rc_proof: Optional[VDFProof]
    timelord_fee_puzzle_hash: Optional[bytes32]
