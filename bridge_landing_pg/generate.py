import json
import os

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def render(template, model):
    tags_html = ''.join(f'<span class="tag">{t}</span>' for t in model['tags'])
    first_name = model['display_name'].split()[0]
    more_count = model['stats']['photos'] + model['stats']['videos'] - 4

    replacements = {
        '{{DISPLAY_NAME}}': model['display_name'],
        '{{FIRST_NAME}}':   first_name,
        '{{SLUG}}':         model['slug'],
        '{{USERNAME}}':     model['username'],
        '{{IMAGE_KEY}}':    model.get('image_key', model['slug']),
        '{{OG_DESCRIPTION}}': model['og_description'],
        '{{AGE}}':          str(model['age']),
        '{{LOCATION}}':     model['location'],
        '{{BIO_PARA1}}':    model['bio'][0],
        '{{BIO_PARA2}}':    model['bio'][1],
        '{{TAGS_HTML}}':    tags_html,
        '{{STAT_PHOTOS}}':  str(model['stats']['photos']),
        '{{STAT_VIDEOS}}':  str(model['stats']['videos']),
        '{{STAT_FANS}}':    str(model['stats']['fans']),
        '{{LIFESTYLE_QUOTE}}': model['lifestyle_quote'],
        '{{MORE_COUNT}}':   str(more_count),
        '{{MSG_PREVIEW}}':  model['msg_preview'],
        '{{PROFILE_URL}}':  model['profile_url'],
    }

    html = template
    for key, val in replacements.items():
        html = html.replace(key, val)
    return html

def main(slugs=None):
    template = load('template.html')
    models = json.loads(load('models.json'))

    if slugs:
        models = [m for m in models if m['slug'] in slugs]

    generated = 0
    for model in models:
        out_path = f"{model['slug']}/index.html"
        save(out_path, render(template, model))
        print(f"  OK  {out_path:<40} ({model['display_name']})")
        generated += 1

    print(f"\nDone. {generated} page(s) generated.")

if __name__ == '__main__':
    import sys
    # Pass slug(s) as args to regenerate specific pages, or no args for all
    # e.g.: python3 generate.py annrose vayanakiss
    slugs = sys.argv[1:] or None
    main(slugs)
