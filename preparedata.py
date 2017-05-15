from tflearn.data_utils import build_hdf5_dataset
import h5py

dataset_file = '/Desktop/Self-Driving-Car/TrainingData/my_dataset.txt'
build_hdf5_image_dataset(dataset_file, image_shape=(128,128), mode='file', ouput_path='/Desktop/Self-Driving-Car/PreparedData/dataset.h5',grayscale=True)
