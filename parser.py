import sys
from argparse import ArgumentParser
from pathlib import Path
import json


def parse_company_attrs(splits, company_dict):
    """
    Takes a given line and extracts appropriate information about the company
    NOTE: This function mutates company_dict in place. Please be mindful of this in debugging

    :param splits: given line (split on ':')
    :type splits: list
    :param company_dict: dictionary of known company attributes
    :type company_dict: dict
    """
    if 'Name' in splits[0]:
        company_dict['name'] = ''.join(splits[1:])
    elif 'Role' in splits[0]:
        company_dict['position'] = ''.join(splits[1:])
    elif 'Summary' in splits[0]:
        company_dict['summary'] = ''.join(splits[1:])
    elif 'Highlight' in splits[0]:
        if 'highlights' in company_dict.keys():
            company_dict['highlights'].append(''.join(splits[1:]))
        else:
            company_dict['highlights'] = [''.join(splits[1:])]
    else:
        print(f'Did not recognize any fields in the following line\n{"".join(splits)}')


def parse_resume_str(text):
    """
    Parses a string of text into a dict (using JSONResume schema)

    :param text: string of text containing resume data
    :type text: str
    :return: dict following JSONResume schema
    :rtype: dict
    """
    lines = text.splitlines()

    name = lines.pop(0) # name will always be the first line

    # default values to initialize
    label, summary = '', ''
    companies = []
    refs = []
    interests = []

    for line in lines:
        splits = line.strip().split(':') # before the colon will be the field name, after is the data

        if 'Job Title' == splits[0]:
            label = label.join(splits[1:])
        elif 'Summary' == splits[0]:
            summary = summary.join(splits[1:])
        elif 'Company' in splits[0]:
            cnum = int(splits[0][splits[0].find('#') + 1])
            if cnum > len(companies): # if this is a new company, add it to the list
                company_dict = {}
                companies.append(company_dict)
            else: # otherwise, grab the pre-existing data on this company
                company_dict = companies[cnum - 1]
            parse_company_attrs(splits, company_dict)
        elif 'Reference' in splits[0]:
            refs.append(''.join(splits[1:]))
        elif 'Interests' in splits[0]: # need the interests to be semicolon separated
            items = ''.join(splits[1:]).strip().split('.')[:-1] # last index is always empty string
            interests.extend(items)
        else:
            print(f'Did not recognize any fields in the following line\n{line}')

    resume_dict = {
        "basics": {
            "name": name.strip(),
            "label": label.strip(),
            "summary": summary.strip()
        },
        "work": companies,
        "references": refs,
        "interests": interests
    }

    return resume_dict


def parse_resume(filename, verbose=False):
    """
    Parses text file containing resume data into a dict (using JSONResume schema)

    :param filename: path to the desired resume text file
    :type filename: str or path-like object
    :param verbose: whether to have verbose output, defaults to False
    :type verbose: bool, optional
    :return: dict following JSONResume schema
    :rtype: dict
    """
    filename = Path(filename) # just to be sure

    with open(filename) as f:
        text = f.read()
        if verbose:
            print(text)

    resume_dict = parse_resume_str(text)
    if verbose:
            print(resume_dict)

    return resume_dict


def main(args=None):
    if len(sys.argv[1:]) > 0:
        parser = ArgumentParser("DeBIAS Resume Parser Enrtypoint")
        parser.add_argument('-f', '--resume-text-file', dest='filename',
                            help='Path to text file containing resume data')
        parser.add_argument('-o', '--output', dest='output',
                            default='resume.json', help='Name of output JSON file')
        parser.add_argument('--verbose', dest='verbose', action='store_true')
        parser.set_defaults(verbose=False)
        args = parser.parse_args()

        filename = args.filename
        output = args.output
        verbose = args.verbose
    else:  
        # Without CLI flags we assume the next token it the file to be read in
        filename = sys.argv[1]

        # Rest of thses are just default vals
        output = 'resume.json'
        verbose = False

    filename = Path(filename)
    output = Path(output)

    resume_dict = parse_resume(filename, verbose=verbose) # parses into dict

    # Saves the dict as a resume
    with open(output, 'w') as f:
        json.dump(resume_dict, f)   
        print(f'Resume parsed into JSON at {output.absolute()}')


if __name__ == "__main__":
    main()
