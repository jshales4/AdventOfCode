# AoC Template

YEAR = 2018
DAY = 3
QUILT_SQUARE_DIMENSIONS = 1000

import re
from typing import Tuple, NamedTuple, List, Optional


class PatternProposal(NamedTuple):
    id: str
    start_x: int
    start_y: int
    x_length: int
    y_length: int


# Part 1
def parse_proposals(patterns: List[str]) -> List[PatternProposal]:
    proposals: List[PatternProposal] = []
    for pattern in patterns:
        match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", pattern)

        proposal = PatternProposal(
            id=match.group(1),
            start_x=int(match.group(2)),
            start_y=int(match.group(3)),
            x_length=int(match.group(4)),
            y_length=int(match.group(5)),
        )
        proposals.append(proposal)
    return proposals


# Part 1
def count_proposal_overlaps(
    proposals: List[PatternProposal],
) -> Tuple[int, Optional[int]]:
    fabric = [
        [0 for _ in range(QUILT_SQUARE_DIMENSIONS)]
        for _ in range(QUILT_SQUARE_DIMENSIONS)
    ]
    overlapping_squares = 0
    possibly_clean_claims: List[int] = []
    for index, proposal in enumerate(proposals):
        is_claim_clean: bool = True
        for y in range(proposal.start_y, proposal.start_y + proposal.y_length):
            for x in range(proposal.start_x, proposal.start_x + proposal.x_length):
                if is_claim_clean and fabric[x][y] != 0:
                    is_claim_clean = False
                if fabric[x][y] == 1:
                    overlapping_squares += 1
                fabric[x][y] += 1
        if is_claim_clean:
            possibly_clean_claims.append(index)

    # Part 2
    clean_id: Optional[int] = None
    for index in possibly_clean_claims:
        proposal = proposals[index]
        if is_proposal_clean(fabric, proposal):
            assert clean_id is None
            clean_id = proposal.id
    return overlapping_squares, clean_id


def is_proposal_clean(fabric, proposal) -> bool:
    for y in range(proposal.start_y, proposal.start_y + proposal.y_length):
        for x in range(proposal.start_x, proposal.start_x + proposal.x_length):
            square = fabric[x][y]
            if square != 1:
                return False
    return True


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    proposals = parse_proposals(data)
    number_of_intersecting_squares, unique_proposal_id = count_proposal_overlaps(
        proposals
    )
    print("Part 1 answer is", number_of_intersecting_squares)
    print("Part 2 answer is", unique_proposal_id)


if __name__ == "__main__":
    main()
