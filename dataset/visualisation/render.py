import open3d as o3d
import os
import numpy as np

current_path = os.path.dirname(__file__)
dir_path = os.path.join(current_path, '../test/mvs_test_00000/')

color = o3d.io.read_image(os.path.join(dir_path, '0000.jpg'))
depth = o3d.io.read_image(os.path.join(dir_path, '0000_depth.png'))

intrinsic_matrix = np.loadtxt(os.path.join(dir_path, 'cam.txt'))

intrinsic = o3d.camera.PinholeCameraIntrinsic()
intrinsic.intrinsic_matrix = intrinsic_matrix

rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(color, depth, convert_rgb_to_intensity = True)
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)

# flip the orientation, so it looks upright, not upside-down
pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])

o3d.io.write_point_cloud(os.path.join(dir_path, '0000.ply'), pcd)
o3d.visualization.draw_geometries([pcd])
