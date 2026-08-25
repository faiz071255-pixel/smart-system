import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("💻 نظام التنبؤ بأعطال الصيانة والتشغيل الذكي")
st.markdown("نظام تخصصي لتحليل وتشخيص احتمالية تعطل الأجهزة بناءً على سجل ساعات التشغيل ودرجات الحرارة.")

data = {
    'Operating_Hours': [500, 1000, 1500, 2000, 2500, 3000],
    'Failure_Risk_Score': [15, 28, 42, 60, 78, 95]
}

df = pd.DataFrame(data)

st.subheader("📊 سجل البيانات التاريخية للأجهزة:")
st.dataframe(df, use_container_width=True)

X = df[['Operating_Hours']]
y = df['Failure_Risk_Score']

model = LinearRegression()
model.fit(X, y)

st.subheader("⚙️ فحص وتشخيص جهاز جديد:")
input_hours = st.slider("حدد عدد ساعات تشغيل الجهاز الحالية:", min_value=100, max_value=5000, value=1200, step=100)

predicted_risk = model.predict([[input_hours]])
risk_value = predicted_risk[0]

if risk_value < 40:
    st.success(f"🟢 حالة الجهاز مستقرة. نسبة خطر العطل المتوقعة: *{risk_value:.1f}%* - الجهاز يعمل بكفاءة.")
elif risk_value < 75:
    st.warning(f"🟡 تنبيه متوسط! نسبة خطر العطل المتوقعة: *{risk_value:.1f}%* - يفضل إجراء صيانة وقائية قريباً.")
else:
    st.error(f"🔴 تنبيه عالي جداً! نسبة خطر العطل المتوقعة: *{risk_value:.1f}%* - الجهاز معرض للتوقف، يجب عمل صيانة فورية!")
