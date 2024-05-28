import itertools
from multiprocessing import Pool, cpu_count
import numpy as np


def volume_of_tetrahedron(p1, p2, p3, p4):
    AB = np.subtract(p2[:3], p1[:3])
    AC = np.subtract(p3[:3], p1[:3])
    AD = np.subtract(p4[:3], p1[:3])
    cross_product = np.cross(AB, AC)
    scalar_triple_product = np.dot(cross_product, AD)
    return abs(scalar_triple_product) / 6.0


def read_points(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip().strip("()")
            x, y, z, n = map(float, line.split(","))
            yield (x, y, z, int(n))


def process_combinations(comb):
    indices, tetra_points = zip(*comb)
    if sum(p[3] for p in tetra_points) == 100:
        volume = volume_of_tetrahedron(*tetra_points)
        return (volume, indices)
    return (float("inf"), None)


def find_smallest_tetrahedron(points):
    min_volume = float("inf")
    best_tetrahedron = None

    combinations = itertools.combinations(enumerate(points), 4)
    with Pool(cpu_count()) as pool:
        results = pool.map(process_combinations, combinations)

    for volume, indices in results:
        if volume < min_volume:
            min_volume = volume
            best_tetrahedron = indices

    return sorted(best_tetrahedron) if best_tetrahedron else None


def main():
    points_small = list(read_points("points_small.txt"))
    points_large = list(read_points("points_large.txt"))

    smallest_tetrahedron_small = find_smallest_tetrahedron(points_small)
    print(f"Indices for points_small.txt: {smallest_tetrahedron_small}")

    smallest_tetrahedron_large = find_smallest_tetrahedron(points_large)
    print(f"Indices for points_large.txt: {smallest_tetrahedron_large}")


if __name__ == "__main__":
    main()
