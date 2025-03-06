import os
import tyro
import numpy as np
import trimesh


@dataclass
class Args:
    mesh_path: str

def main(mesh_path):
    mesh = trimesh.load_mesh(mesh_path)

    # Modify T as necessary such that z-axis is pointing upwards
    T = trimesh.transformations.rotation_matrix(-np.pi/2, [1, 0, 0])
    T[:3, 3] = -mesh.centroid

    print(f"mesh.centroid = {mesh.centroid}")
    mesh.apply_transform(T)

    T2 = trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0])
    mesh.apply_transform(T2)

    dir, filename = os.path.split(mesh_path)
    new_filename = filename.replace(".obj", "_new.obj")
    mesh.export(os.path.join(dir, new_filename))
    print(f"Saved to: {os.path.join(dir, new_filename)}")

if __name__=="__main__":
    args = tyro.cli(Args)
    main(args.mesh_path)