#!/usr/bin/python3

import pandas

def main():
    json = pandas.read_json("5movies.json")
    json.to_csv("5movies-JSON2CSV.csv")

if __name__ == "__main__":
    main()

