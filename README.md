# UMD DeBIAS Resume Parsing

## Parsing Resumes
For parsing text files into resume JSONs, use ```parser.py```

Example:
```python parser.py -f /path/to/resume/text/file.txt -o /path/to/ouput.json```

Arguments are as follows:
- ```-f```  or ```--resume-text-file```  is the path to the text file to be parsed
- ```-o``` or ```--output``` is the desire output JSON's filename (defaults to ```resume.json```)
- ```--verbose``` enables output of the parsed resume