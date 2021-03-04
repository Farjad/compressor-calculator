import compressors

compressor_one = compressors.CompressorOne("NameOne")
compressor_two = compressors.CompressorTwo("NameTwo")


compressors = []

compressors.append(compressor_one)
compressors.append(compressor_two)


for compressor in compressors:
    print("Compressor: %s" % compressor.get_name())
