# General settings

# This will delete intermediate files
# It will make full analysis from scratch take longer
# but free up disk space
delete_intermediates = False

# 1. FOR LOADING NEW DATA

# The directory where your raw files are held (can be zip files)
# This can be either relative or absolute path
rawFilesDir = "../raw_files"

# The Qscore_threshold to use
# This must be defined (use -1 if do not want to filter)
Qscore_threshold = 20


# 2. FOR FINGERPRINTING

# The R flank sequence to look for
flank_sequence = "TGTTGGAACAACCAT"

# The length of the fingerprint to match (set by restriction enzyme)
fingerprint_length = 17


# 3. FOR MAPPING

# The number of bases duplicated by transposon insertion
transposon_site_duplication_length = 5

# The path to the genome file to use for read alignment
genome_path = "../Example/genome.fasta"