

{% macro dialog() -%}
    Please state {{ session.p_name or "the patient's"}} Phone Number.
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
    <input type="text" name="p_msisdn" placeholder="Patient's Phone No">
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    CANCEL CALL
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}

