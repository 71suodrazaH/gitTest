import os

# Paths for input, output, and reference directories
input_file = "inputs/test_vectors.txt"
output_file = "outputs/results.txt"
expected_file = "reference/expected_results.txt"

# Ensure the output directory exists
os.makedirs("outputs", exist_ok=True)

# Step 1: Read test vectors
try:
    with open(input_file, "r") as f:
        vectors = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Error: {input_file} not found!")
    exit(1)

# Step 2: Simulate processing (e.g., applying logical AND and XOR)
results = []
for vector in vectors:
    try:
        a, b = map(int, vector.split())
        and_result = a & b
        xor_result = a ^ b
        results.append(f"{a} {b} -> AND: {and_result}, XOR: {xor_result}")
    except ValueError:
        print(f"Invalid input vector: {vector}")

# Write results to output file
with open(output_file, "w") as f:
    f.write("\n".join(results))
print(f"Results written to {output_file}")

# Step 3: Compare with expected results
try:
    with open(expected_file, "r") as f:
        expected_results = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Warning: {expected_file} not found! Skipping verification.")
    exit(0)

# Check results match
mismatches = []
for i, (result, expected) in enumerate(zip(results, expected_results)):
    if result != expected:
        mismatches.append((i + 1, result, expected))

# Print verification summary
if not mismatches:
    print("Verification passed: All results match expected values!")
else:
    print("Verification failed:")
    for idx, result, expected in mismatches:
        print(f"Line {idx}: Result = {result} | Expected = {expected}")
