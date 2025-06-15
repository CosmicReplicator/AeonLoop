# _plugins/fence_to_mermaid.rb
# Transform ```mermaid fences into {% mermaid %} … {% endmermaid %}

Jekyll::Hooks.register [:pages, :documents], :pre_render do |doc|
  doc.content.gsub!(/```mermaid\s+([\s\S]*?)\s+```/m) do
    "{% mermaid %}\n#{$1}\n{% endmermaid %}"
  end
end
