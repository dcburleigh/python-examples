
from jinja2 import Template

fn = 'ex1'
fn = 'ex0';

tf = 'templates/%s.tpl.html' % fn
hf = '%s.html' % fn
with open(tf, 'r') as th:
    tpl = th.read()

word_list = [ 'apple', 'banana', 'cherry']
with open(hf, 'w') as hh:
    template = Template( tpl )
    hh.write( template.render(my_string='abcd', my_list=word_list))

print("wrote: %s" % hf )
