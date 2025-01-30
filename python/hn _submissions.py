from operator import itemgetter
import requests
import plotly.express as px

def get_hackernews_data():

    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    submission_ids = r.json()


    submission_dicts = []
    for submission_id in submission_ids[:5]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),  
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")

    return submission_dicts

def create_visualization(submission_dicts):
    titles = [d['title'] for d in submission_dicts]
    comments = [d['comments'] for d in submission_dicts]

    fig = px.bar(
        x=titles,
        y=comments,
        title="Top Hacker News Stories by Comments",
        labels={'x': 'Story Title', 'y': 'Number of Comments'}
    )

    fig.update_layout(
        title_font_size=28,
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickangle=45  
    )

    return fig

def main():
    submission_dicts = get_hackernews_data()
    fig = create_visualization(submission_dicts)
    fig.show()

if __name__ == "__main__":
    main()