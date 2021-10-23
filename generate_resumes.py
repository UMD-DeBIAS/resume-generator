import json
from argparse import ArgumentParser
from pathlib import Path

from tqdm import trange
import openai

from keys import OPENAI_API_KEY
from parser import parse_resume_str


def generate_resume_text(gpt_request_file):
    with open(gpt_request_file, 'r') as f:
        gpt_request = f.read()

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        engine="davinci",
        prompt=gpt_request,
        temperature=0.8,
        max_tokens=896,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["====="]
    )

    text = response["choices"][0]["text"]
    
    return text


def main(args=None):
    parser = ArgumentParser("DeBIAS Resume Generator Entrypoint")
    parser.add_argument('-n', '--num-resumes', dest='num_resumes', type=int, default=1, help='number of resumes to generate (default is 1)')
    parser.add_argument('-f', '--request-file', dest='gpt_request_file', help='Path to text file containing desired input for GPT3')
    parser.add_argument('-o', '--output-dir', dest='output_dir', default='.', help='Directory to output resume JSONs to (default is CWD)')
    args = parser.parse_args()

    gpt_request_file = Path(args.gpt_request_file)
    num_resumes = args.num_resumes
    output_dir = Path(args.output_dir)
    fail_dir = output_dir / 'fails'

    if not output_dir.exists():
        output_dir.mkdir()
    if not fail_dir.exists():
        fail_dir.mkdir()

    fail_count = 0
    for _ in trange(num_resumes, desc="Generating Resumes"):
        resume_text = generate_resume_text(gpt_request_file)
            
        try:
            resume_dict = parse_resume_str(resume_text)
            
            filename = output_dir / f"{resume_dict['basics']['name'].strip().replace(' ', '_')}.json"
            with open(filename, 'w') as f:
                json.dump(resume_dict, f, indent=4, separators=(',', ': '))
        except Exception as e:
            fail_count += 1
            with open(fail_dir / f'fail{fail_count}.txt', 'w') as f:
                f.write(resume_text)
        
        

    print(f'{num_resumes - fail_count} resumes generated and saved to {output_dir}')
    print(f'{fail_count} failed to parse')


if __name__ == '__main__':
    main()
