# MhankBarBar
from requests import get
import html_text
def cordIndo(q):
	try:
		id_ = get('http://app.chordindonesia.com/?json=get_search_results&exclude=date,modified,attachments,comment_count,comment_status,thumbnail,thumbnail_images,author,excerpt,content,categories,tags,comments,custom_fields&search=%s' % q).json()['posts'][0]['id']
		chord = get('http://app.chordindonesia.com/', params={"json":"get_post","id":id_}).json()
		result = html_text.parse_html(chord['post']['content']).text_content()
		return result
	except Exception as e:
		print(e)
		return "[❗] Maaf chord yang anda cari tidak dapat saya temukan"