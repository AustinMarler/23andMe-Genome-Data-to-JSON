import json
snps = {"snps":[]}

genome = open("genome.txt")
columns = ["rsid", "chromosome", "position", "genotype"]

for line in genome:
    line = line.strip()
    if line.startswith("#"):
        pass
    else:
        d = {}
        data = [item.strip() for item in line.split('\t')]
        for index, elem in enumerate(data):
            d[columns[index]] = data[index]
            
        snps["snps"].append(d)
    
genome.close()

genome_json = open("genome.json", "w")
genome_json.write(json.dumps(snps, indent=4))
genome_json.close()