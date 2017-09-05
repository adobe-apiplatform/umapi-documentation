# Navigation Generator is a Jekyll plugin that extracts H2 headings from each page so that it can be used as part of the generation of the navigation menu.
#
# How To Use:
#   1.) Copy source file into your _plugins folder within your Jekyll project.
#   2.) When generating the navigation menu, refer to the sub headings as:
#      <ul>
#          {% for item in my_page.subnav %}
#               <li><a href="{{ item.url }}">{{ item.title }}</a></li>
#          {% endfor %}
#      </ul>
#   3.) Run Jekyll: jekyll --server to re-generate your site.
#
# Author: Lea Savage
# Referenced Site: http://blog.honeybadger.io/automatically-generating-subnavigation-from-headings-in-jekyll/

require "nokogiri"

class MySubnavGenerator < Jekyll::Generator
  def generate(site)
    parser = Jekyll::Converters::Markdown.new(site.config) 

    site.pages.each do |page|
      if page.ext == ".md"
        doc = Nokogiri::HTML(parser.convert(page['content']))
        page.data["subnav"] = []
        doc.css('h2').each do |heading|
          page.data["subnav"] << { "title" => heading.text, "url" => [page.url, heading['id']].join("#") }  
        end
      end
    end
  end
end