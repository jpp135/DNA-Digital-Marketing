import pandas as pd
import streamlit as st

url = "https://app.mindstudio.ai/agents/untitled-ai-agent-6db49a39/run?draftVersionId=074b8a8b-db09-4f25-bc1d-7765026292d1"
video_url = "https://www.youtube.com/watch?v=1g-t8gHicIs"

st.title("Welcome to TYS Accounting Solutions")
st.image("tys 2.webp")

#who we are text
st.title("\n\nWho We Are")
st.text("TYS LLP is a full-service CPA firm with offices in Fairport, New York and Walnut Creek, California. We're not your typical accounting firm — we're built on the belief that accounting should be dynamic, collaborative, and innovative.\nWe specialize in providing comprehensive audit, tax, and consulting services to a diverse group of individuals and businesses, with particular depth in two areas that set us apart: construction accounting and business consulting. With over 60 years of combined construction market experience, we've built a successful track record working with construction bankers and established credibility with bonding agents — giving our construction clients a genuine competitive edge.\nBeyond the numbers, we serve as trusted advisors, taking a personal stake in our clients' success. We pride ourselves on developing meaningful relationships and delivering exceptional service to help our clients achieve their financial goals. Our clients love the fact that we don't track billable hours, and we guarantee our pricing — because we'd rather focus on results than timesheets.\nAt TYS, we know it's people that are worth counting.")
st.video(data = video_url)
st.text("A message from founding partner Chris Yorke")

#services text
st.title("Our Services")
st.text("> Construction Accounting — Specialized accounting for construction businesses, leveraging 60+ years of industry experience to improve profitability, support bonding, and navigate construction-specific tax challenges.\n> Income Tax Planning & Preparation — Full-service tax planning and preparation for businesses and individuals, focused on minimizing tax liability while keeping clients compliant with current tax laws.\n> Financial Statements — Audit, review, and compilation services backed by thorough analysis of past and present financial performance, plus strategic advisory.\n> Accounting Services — Comprehensive, customized accounting support that goes beyond the basics — acting as an extension of your business to drive improvements and efficiencies.\n> Business Consulting — Strategic consulting services delivered in actionable steps, including due diligence, opportunity assessment, strategic planning, and performance metrics tied to your financial goals.\n> Operating Practices & Procedures — Help building and streamlining standard operating procedures, communication structures, and accountability systems across your organization.")

#customers
st.title("Customers We Serve")
st.text("> Closely Held Firms & Family-Owned Business\nTYS serves as a trusted advisor to small business owners, including family-owned companies. \nBacked by comprehensive knowledge and core values, our team becomes an asset that strengthens your business, empowering you to address the difficult financial decisions that pop up every day.\nWe provide a range of services for every stage of your business, from bookkeeping basics, to business formation, to Sustainable Succession.\n\n> Construction Firms\nConstruction Accounting is complicated.\nTYS provides a competitive advantage by delivering over 60 years of construction market experience to its clients.\nBeyond our thorough understanding of the industry, we maintain strong relationships with legal, banking, bonding, and other critical firms and agencies.\nWe understand the unique tax rules and alternatives that impact construction companies.\nWhether you are looking for ways to better manage your projects, fine-tune your estimates or satisfy your bonding company, we partner with you to reduce the costs of doing business while maintaining compliance.\n\n> Individuals and Families\nAt TYS we know life can get complicated in a hurry.\nThat’s why our team of professionals are here to address your unique needs, sharing insight and answers whenever you need us.\nThat means throughout the year and into the future.\nOur team can help with the preparation for college savings, trusts, real estate, taxes and other important family matters.\nOur goal is to help plan for now and into the future to give you peace of mind to enjoy life to the fullest.")

#chatbot
st.link_button("Speak with our automated assistant", url)

#TODO: Tunnel streamlit app so it's accessible from the web
