import h5py
filenames = ["train.hdf5", "val.hdf5", "test.hdf5"]
for filename in filenames:
    db = h5py.File(filename, "r")
    print(db["images"].shape)
    db.close()
