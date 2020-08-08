import pytest
from aoc_2018_03 import parse_proposals, PatternProposal, count_proposal_overlaps


def test_parse_line():
    assert parse_proposals(["#123 @ 3,2: 5x4"]) == [PatternProposal("123", 3, 2, 5, 4)]


def test_count_proposal_overlaps():
    proposal_strings = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    proposals = parse_proposals(proposal_strings)
    number_of_overlapping_squares, non_intersecting_claim_id = count_proposal_overlaps(
        proposals
    )
    assert number_of_overlapping_squares == 4
    assert non_intersecting_claim_id == "3"
