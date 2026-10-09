def read_fasta(filename):
    records = []
    current_header = None
    current_sequence = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_header is not None:
                    sequence = "".join(current_sequence).upper()
                    records.append((current_header, sequence))
                current_header = line[1:].strip()
                current_sequence = []
            else:
                if current_header is None:
                    raise ValueError(
                        "Sequence data found before a FASTA header."
                    )
                current_sequence.append(
                    "".join(line.split())
                )
    if current_header is not None:
        sequence = "".join(current_sequence).upper()
        records.append((current_header, sequence))
    if not records:
        raise ValueError("No FASTA records found in the file.")
    return records
def analyze_sequence(sequence):
    valid_bases = set("ATGC")
    invalid_bases = sorted(set(sequence) - valid_bases)
    counts = {
        base: sequence.count(base)
        for base in "ATGC"
    }
    gc_count = counts["G"] + counts["C"]
    if sequence and not invalid_bases:
        gc_percent = gc_count / len(sequence) * 100
    else:
        gc_percent = None
    return {
        "length": len(sequence),
        "counts": counts,
        "gc_percent": gc_percent,
        "valid": len(sequence) > 0 and not invalid_bases,
        "invalid_bases": invalid_bases,
    }
def main():
    filename = input("Enter FASTA filename: ").strip()
    try:
        records = read_fasta(filename)
        print("\n" + "=" * 40)
        print(" FASTA ANALYZER REPORT")
        print("=" * 40)
        print("Total records:", len(records))
        for number, (header, sequence) in enumerate(records, start=1):
            result = analyze_sequence(sequence)
            accession = header.split()[0] if header else "Unknown"
            print("\n" + "-" * 40)
            print(f"Record {number}: {header}")
            print("Accession:", accession)
            print("Sequence length:", result["length"])
            print("Base counts:", result["counts"])
            if result["gc_percent"] is not None:
                print(f'GC content: {result["gc_percent"]:.2f}%')
            else:
                print("GC content: Not available (invalid or empty sequence)")
            print("Valid DNA:", "Yes" if result["valid"] else "No")
            if result["invalid_bases"]:
                print("Unexpected characters:", result["invalid_bases"])
        print("\n" + "=" * 40)
        print("Analysis complete!")
        print("=" * 40)
    except FileNotFoundError:
        print("Error: File not found. Check the filename and try again.")
    except (ValueError, OSError) as error:
        print("Error:", error)
if __name__ == "__main__":
    main()