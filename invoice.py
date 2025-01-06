import streamlit as st
import pandas as pd

invoice_no = st.sidebar.text_input('Invoice No.')
invoice_date = st.sidebar.date_input('Date', format='YYYY-MM-DD')

st.sidebar.divider()

st.sidebar.header('Billed To:')

billed_to_name = st.sidebar.text_input('Name', placeholder='Tan Wei Ming')
billed_to_address_1 = st.sidebar.text_input('Address Line 1', placeholder='123, Jalan Bukit Bintang,')
billed_to_address_2 = st.sidebar.text_input('Address Line 2 (optional)', placeholder='Taman Pelangi Indah,')
billed_to_zip = st.sidebar.text_input('Zip/Postal Code', placeholder='55100')
billed_to_city = st.sidebar.text_input('City', placeholder='Kuala Lumpur')
billed_to_state = st.sidebar.text_input('State/Province', placeholder='Wilayah Persekutuan')
billed_to_country = st.sidebar.text_input('Country', placeholder='Malaysia')

st.sidebar.divider()

st.sidebar.header('Content')

content_df = pd.DataFrame([
    {"description": "Eggshell Camisole Top", "fee": 123.40},
    {"description": "Cuban Collar Shirt", "fee": 254.09},
    {"description": "Floral Cotton Dress", "fee": 123.00},
])

edit_df_config = {
    'description': st.column_config.TextColumn('Description', required=True),
    'fee': st.column_config.NumberColumn('Fee', min_value=0, step=0.01, required=True)
}
edited_content_df = st.sidebar.data_editor(
    content_df,
    num_rows="dynamic",
    column_config=edit_df_config,
    use_container_width=True
)

total_fee = edited_content_df['fee'].sum()

# Actual content
@st.cache_data
def get_html_template():
    with open('template.html', 'r') as f:
        template = f.read()
    return template

# Get the template
invoice_html_template = get_html_template()

# Format the address
address_parts = [
    billed_to_name,
    billed_to_address_1,
    billed_to_address_2,
    f"{billed_to_zip} {billed_to_city}, {billed_to_state}",
    billed_to_country
]
formatted_address = '<br>'.join(part.strip() for part in address_parts if part and part.strip())

# Format the date
formatted_date = invoice_date.strftime("%b %d, %Y").replace(" 0", " ")

# Create table rows for items
item_rows = ""
for _, row in edited_content_df.iterrows():  # Changed from content_df to edited_content_df
    item_rows += f"""            <tr>
            <td>{row['description']}</td>
            <td>{row['fee']:.2f}</td>
        </tr>\n"""

# Create replacements dictionary
replacements = {
    '{{INVOICE_NO}}': invoice_no if invoice_no else '',
    '{{INVOICE_DATE}}': formatted_date,
    '{{BILLED_TO_ADDRESS}}': formatted_address,
    '{{ITEM_ROWS}}': item_rows,
    '{{TOTAL_AMOUNT}}': f'{total_fee:.2f}'  # Changed from total to total_fee
}

# Perform all replacements
invoice_html_content = invoice_html_template
for placeholder, value in replacements.items():
    invoice_html_content = invoice_html_content.replace(placeholder, str(value))

# Debug output
# st.write("Replacements:", replacements)
# st.write("Template contains INVOICE_NO:", '{{INVOICE_NO}}' in invoice_html_template)
# st.write("Template contains INVOICE_DATE:", '{{INVOICE_DATE}}' in invoice_html_template)
# st.write("Template contains BILLED_TO_ADDRESS:", '{{BILLED_TO_ADDRESS}}' in invoice_html_template)

st.header("Preview")
st.components.v1.html(invoice_html_content, height=1000)

st.header("HTML Code")
st.code(invoice_html_content)