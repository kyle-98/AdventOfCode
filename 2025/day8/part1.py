from math import sqrt

class Point:
    def __init__(self, x: int, y: int, z: int, circuit: int):
        self.X = float(x)
        self.Y = float(y)
        self.Z = float(z)
        self.Circuit = circuit

    def __repr__(self):
        return f'Point(X={self.X}, Y={self.Y}, Z={self.Z}, Circuit={self.Circuit})'
    

class PointPair:
    def __init__(self, point1: Point, point2: Point, distance: int = 0):
        self.Point1 = point1
        self.Point2 = point2
        self.Distance = distance

    def __repr__(self):
        return f'PointPair(Point1={self.Point1}, Point2={self.Point2}, Distance={self.Distance})'
    

class PointPairManager:
    def __init__(self):
        self._point_pairs = set()
    
    def add_point_pair(self, point_pair: 'PointPair'):
        self._point_pairs.add(point_pair)

    def get_count(self) -> int:
        return len(self._point_pairs)

    def get_all(self):
        return self._point_pairs


def calculate_distance(point_1: Point, point_2: Point) -> float:
    return sqrt(
        ((point_2.X - point_1.X) ** 2) + 
        ((point_2.Y - point_1.Y) ** 2) +
        ((point_2.Z - point_1.Z) ** 2)
    )


def find_root(idx: int, circuit_root: list[range]) -> int:
    if circuit_root[idx] == idx:
        return idx
    
    circuit_root[idx] = find_root(circuit_root[idx], circuit_root)
    return circuit_root[idx]


def join_circuits(point1_idx: int, point2_jdx: int, circuit_root: list[range], circuit_size: list[int]) -> bool:
    root_point1 = find_root(point1_idx, circuit_root)
    root_point2 = find_root(point2_jdx, circuit_root)

    if root_point1 == root_point2:
        return False
    
    if circuit_size[root_point1] < circuit_size[root_point2]:
        circuit_root[root_point1] = root_point2
        circuit_size[root_point2] += circuit_size[root_point1]
    else:
        circuit_root[root_point2] = root_point1
        circuit_size[root_point1] += circuit_size[root_point2]

    return True


if __name__ == '__main__':
    TARGET_CONNECTIONS = 1000
    with open('input.txt', 'r') as f:
        data = [Point(*line.strip().split(','), circuit=idx) for idx, line in enumerate(f)]

    stored_point_pairs = PointPairManager()

    for point1_idx in range(len(data)):
        for point2_idx in range(point1_idx + 1, len(data)):
            point1 = data[point1_idx]
            point2 = data[point2_idx]

            stored_point_pairs.add_point_pair(
                PointPair(
                    point1,
                    point2,
                    calculate_distance(point1, point2)
                )
            )

    sorted_point_pairs: list['PointPair'] = sorted(stored_point_pairs.get_all(), key=lambda pp: pp.Distance)
    circuit_root = list(range(len(data)))
    circuit_size = [1] * len(data)
    total_connections = 0

    for point_pair in sorted_point_pairs:
        point1 = point_pair.Point1
        point2 = point_pair.Point2

        if total_connections == TARGET_CONNECTIONS:
            break
        join_circuits(point1.Circuit, point2.Circuit, circuit_root, circuit_size)
        total_connections += 1
    
    final_circuts_sizes = []

    for idx in range(len(data)):
        if circuit_root[idx] == idx:
            final_circuts_sizes.append(circuit_size[idx])

    final_circuts_sizes.sort(reverse=True)

    print(final_circuts_sizes)
    print('>>', final_circuts_sizes[0] * final_circuts_sizes[1] * final_circuts_sizes[2])