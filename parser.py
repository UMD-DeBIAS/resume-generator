import re

def get_interests(txt):
  interests_txt = None
  if re.search('Interests: (.+)\n', txt):
    interests_txt = re.search('Interests: (.+)\n', txt).group(1)
  else: #Case where there are no interests
    return []
  interests = interests_txt.split('. ')
  if interests[-1] == '.':
    interests[-1] = interests[-1][:-1] #Gets rid of trailing period
  return [{"name": interest} for interest in interests]


def get_name(txt, num):
  if re.search('Company #'+ str(num) + ' Name:(.+)\n', txt):
    return re.search('Company #'+ str(num) + ' Name:(.+)\n', txt).group(1)
  else:
    return re.findall('Company #'+ str(num) + ':(.+)\n', txt)[0]

def get_role(txt, num):
  if re.search('Company #'+ str(num), txt):
    if re.search('Company #'+ str(num) + ' Role:(.+)\n', txt):
      return re.search('Company #'+ str(num) + ' Role:(.+)\n', txt).group(1)
    else:
      return re.findall('Company #'+ str(num) + ':(.+)\n', txt)[1]
  else:
    return re.findall('Job Title:(.)+\n', txt)[num]

def get_summary(txt, num):
  if re.search('Company #'+ str(num) + ' Summary:(.+)\n', txt):
    return re.search('Company #'+ str(num) + ' Summary:(.+)\n', txt).group(1)
  else:
    return re.search('Summary:(.+)\n', txt).group(1)

def main(filename):
    with open(filename) as f:
        text = f.readlines()
        text = ''.join(text)
    print(text)
    deliverable = {
        "basics": {
            "name": re.search('^([\w\s]+)\n', text).group(1),
            "label": re.search('Job Title:([\w\s]+)\n', text).group(1),
            "summary": re.search('Summary:(.+)\n', text).group(1)
        },
        "work": [{
            "name": get_name(text, 1),
            "position": get_role(text, 1),
            "summary": get_summary(text, 1),
            "highlights": [
                re.search('Company #1[\s|:]Highlight 1:(.+)\n', text).group(1),
                re.search('Company #1[\s|:]Highlight 2:(.+)\n', text).group(1),
            ]
        },
            {
                "name": get_name(text, 2) if re.search('Company #2', text) else None,
                "position": get_role(text, 2) if re.search('Company #2', text) else None,
                "summary": get_summary(text, 2) if re.search('Company #2', text) else None,
                "highlights": [
                    re.search('Company #2[\s|:]Highlight 1:(.+)\n', text).group(1) if re.search('Company #2',
                                                                                                text) else None,
                    re.search('Company #2[\s|:]Highlight 2:(.+)\n', text).group(1) if re.search('Company #2',
                                                                                                text) else None,
                ]
            }],
        "references": [{
            "reference": re.search('Personal Reference:(.+)\n', text).group(1)
        }],
        "interests": get_interests(text)
    }

    print(deliverable)


    return deliverable


if __name__ == "__main__":
    main("example-gen.txt")