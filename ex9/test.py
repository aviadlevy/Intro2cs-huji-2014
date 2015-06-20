
with open(args.infile, "rb") as compressed_file:
    binary_text = list(compressed_file.read())

for compression in range(compress_level):
    get_data = hzlib.symbol_count(binary_text)
    huff_tree = hzlib.make_huffman_tree(get_data)
    codebook = hzlib.build_codebook(huff_tree)
    canbook = hzlib.build_canonical_codebook(codebook)
    bits = hzlib.compress(binary_text, canbook)
    byteseq = hzlib.pad(bits)
    compressed_file = list(hzlib.join(byteseq, canbook))

    if args.alwayscompress:
        binary_text = compressed_file
    else:
        if len(binary_text) < len(compressed_file):
            compressed_file = binary_text
            compress_level = compression
            break
    compressed_file = list(hzlib.MAGIC) + [compress_level] + \
                      list(compressed_file)

    if args.outfile is None:
        file_name = args.infile + args.suffix
    else:
        file_name = args.outfile
    if not args.force:
        if os.path.isfile(file_name):
            raise FileExistsError

    with open(file_name, "wb") as output:
        output.write(bytearray(compressed_file))
