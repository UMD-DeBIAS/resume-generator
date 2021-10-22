# UMD DeBIAS Resume Parsing

## Parsing Resumes
For parsing text files into resume JSONs, use ```parser.py```

Example:
```python parser.py -f /path/to/resume/text/file.txt -o /path/to/output.json```

Arguments are as follows:
- ```-f```  or ```--resume-text-file```  is the path to the text file to be parsed
- ```-o``` or ```--output``` is the desired output JSON's filename (defaults to ```resume.json```)
- ```--verbose``` enables output of the parsed resume
  
## Generating Resumes
To generate resume JSONs with GPT3, use ```generate_resumes.py```

Example:
```python generate_resumes.py -f /path/to/gpt3/request.txt -n 5 -o /path/to/output/directory/```

Arguments are as follows:
- ```-f```  or ```--request-file```  is the path to the text file containing the request to GPT3
- ```-o``` or ```--output-dir``` is the path to the desired output directory for all generated JSONs 
- ```-n``` or ```--num-resumes``` is the number of resumes to generate
