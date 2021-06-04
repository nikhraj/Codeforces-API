from lxml import html 
import requests 


def parse_contest(contest_link):
    page = requests.get(contest_link).text
    tree = html.fromstring(page.content)
    contest = {
        "contest_id": get_contest_id(tree),
        "problems": get_problems(tree),
       
    }
    return contest

def get_contest_id(tree):
    contest_link = tree.xpath('//*[@id="sidebar"]/div[1]/table/tbody/tr[1]/th/a/@href')
    return int(contest_link[0].split('/')[2]) if len(contest_link) else 0

def get_problems(tree):
    problems = []

    problem_links = tree.xpath('//*[@class="problems"]/tr/td[2]/div/div[1]/a/@href')
    problem_names = tree.xpath('//*[@class="problems"]/tr/td[2]/div/div[1]/a/text()')

    for i in range(len(tree.xpath('//*[@class="problems"]/tr/td[2]/div/div[1]/a/text()'))):
        problem = {}
        problem["problem_id"] = problem_links[i].split('/')[4]
        problem["contest_id"] = int(problem_links[i].split('/')[2])
        problem["name"] = problem_names[i]
        problem["problem_link"] = problem_links[i]
        
        problems.append(problem)
    
    return problems
