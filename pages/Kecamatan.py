import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Adminduk Jabar', layout='wide')

with st.container(border=True):
    with st.container(border=True):
        st.title(':blue[Administrasi Kependudukan] :green[Jawa Barat] :orange[Semester 1 2024]')
        st.caption('Sumber: https://gis.dukcapil.kemendagri.go.id/peta/')

st.subheader('', divider='orange')

from data import pilihankab
from data import datapenduduk

kol1, kol2 = st.columns(2)
with kol1:
    kabterpilih = st.selectbox('Pilih Wilayah', pilihankab)

with kol2:
    kec = datapenduduk[datapenduduk['Kabupaten/Kota'] == kabterpilih]['Kecamatan'].unique()
    kecterpilih = st.selectbox('Pilih Kecamatan', kec)

if kabterpilih and kecterpilih:
    penduduk = datapenduduk[(datapenduduk['Kabupaten/Kota'] == kabterpilih) & (datapenduduk['Kecamatan'] == kecterpilih)]
    penduduk2 = penduduk.groupby(['Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'])['Jumlah Penduduk'].sum().reset_index()
    keluarga = penduduk.groupby(['Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'])['Jumlah Kepala Keluarga'].sum().reset_index()

with st.container(border=True):
    st.subheader(f'Jumlah Penduduk Kecamatan :orange[{kecterpilih}, {kabterpilih}]')
    kol1a, kol1b = st.columns(2)
    with kol1a:
        with st.container(border=True):
            penduduk3 = penduduk2.sort_values(by='Jumlah Penduduk', ascending=False)
            bar_penduduk = px.bar(penduduk3, x='Jumlah Penduduk', y='Kelurahan/Desa')
            st.plotly_chart(bar_penduduk, use_container_width=True)
    
    with kol1b:
        with st.container(border=True):
            pie_penduduk = px.pie(penduduk3, values='Jumlah Penduduk', color='Kelurahan/Desa')
            st.plotly_chart(pie_penduduk, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(penduduk3, hide_index=True, use_container_width=True)

st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader(f'Jumlah KK Kecamatan :orange[{kecterpilih}, {kabterpilih}]')
    kol2a, kol2b = st.columns(2)
    with kol2a:
        with st.container(border=True):
            keluarga2 = keluarga.sort_values(by='Jumlah Kepala Keluarga', ascending=False)
            bar_keluarga = px.bar(keluarga2, x='Jumlah Kepala Keluarga', y='Kelurahan/Desa')
            st.plotly_chart(bar_keluarga, use_container_width=True)
    
    with kol2b:
        with st.container(border=True):
            pie_keluarga = px.pie(keluarga2, values='Jumlah Kepala Keluarga', color='Kelurahan/Desa')
            st.plotly_chart(pie_keluarga, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(keluarga2, hide_index=True, use_container_width=True)
        
st.subheader('', divider='orange')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['Jenis Kelamin', 'Status Kawin', 'Agama', 
                                                          'Kelompok Umur', 'Pendidikan', 'Golongan Darah', 
                                                          'Usia Pendidikan', 'Pekerjaan'])

with tab1:
    from data import datajeniskelamin2
    jeniskelamin2 = datajeniskelamin2[(datajeniskelamin2['Kabupaten/Kota'] == kabterpilih) & (datajeniskelamin2['Kecamatan'] == kecterpilih)]
    jeniskelamin3 = jeniskelamin2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Jenis Kelamin'])['Jumlah Penduduk'].sum().reset_index()
    trimep1 = px.treemap(jeniskelamin3, path=['Kecamatan', 'Kelurahan/Desa', 'Jenis Kelamin'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep1, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(jeniskelamin3, hide_index=True, use_container_width=True)

with tab2:
    from data import datastatuskawin2
    statuskawin2 = datastatuskawin2[(datastatuskawin2['Kabupaten/Kota'] == kabterpilih) & (datastatuskawin2['Kecamatan'] == kecterpilih)]
    statuskawin = statuskawin2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Status Kawin'])['Jumlah Penduduk'].sum().reset_index()
    trimep2 = px.treemap(statuskawin, path=['Kecamatan', 'Kelurahan/Desa', 'Status Kawin'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep2, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(statuskawin, hide_index=True, use_container_width=True)
            
with tab3:
    from data import dataagama2
    agama2 = dataagama2[(dataagama2['Kabupaten/Kota'] == kabterpilih) & (dataagama2['Kecamatan'] == kecterpilih)]
    agama = agama2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Agama'])['Jumlah Penduduk'].sum().reset_index()
    trimep3 = px.treemap(agama, path=['Kecamatan', 'Kelurahan/Desa', 'Agama'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep3, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(agama, hide_index=True, use_container_width=True)
            
with tab4:
    from data import dataumur2
    umur2 = dataumur2[(dataumur2['Kabupaten/Kota'] == kabterpilih) & (dataumur2['Kecamatan'] == kecterpilih)]
    umur = umur2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Kelompok Umur'])['Jumlah Penduduk'].sum().reset_index()
    trimep4 = px.treemap(umur, path=['Kecamatan', 'Kelurahan/Desa', 'Kelompok Umur'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep4, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(umur, hide_index=True, use_container_width=True)
            
with tab5:
    from data import datapendidikan2
    pendidikan2 = datapendidikan2[(datapendidikan2['Kabupaten/Kota'] == kabterpilih) & (datapendidikan2['Kecamatan'] == kecterpilih)]
    pendidikan = pendidikan2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Pendidikan'])['Jumlah Penduduk'].sum().reset_index()
    trimep5 = px.treemap(pendidikan, path=['Kecamatan', 'Kelurahan/Desa', 'Pendidikan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep5, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pendidikan, hide_index=True, use_container_width=True)
            
with tab6:
    from data import datagolongandarah2
    goldar2 = datagolongandarah2[(datagolongandarah2['Kabupaten/Kota'] == kabterpilih) & (datagolongandarah2['Kecamatan'] == kecterpilih)]
    goldar = goldar2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Golongan Darah'])['Jumlah Penduduk'].sum().reset_index()
    trimep6 = px.treemap(goldar, path=['Kecamatan', 'Kelurahan/Desa', 'Golongan Darah'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep6, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(goldar, hide_index=True, use_container_width=True)
            
with tab7:
    from data import datausiadidik2
    usia2 = datausiadidik2[(datausiadidik2['Kabupaten/Kota'] == kabterpilih) & (datausiadidik2['Kecamatan'] == kecterpilih)]
    usia = usia2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Usia Pendidikan'])['Jumlah Penduduk'].sum().reset_index()
    trimep7 = px.treemap(usia, path=['Kecamatan', 'Kelurahan/Desa', 'Usia Pendidikan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep7, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(usia, hide_index=True, use_container_width=True)
            
with tab8:
    from data import datapekerjaan2
    pekerjaan2 = datapekerjaan2[(datapekerjaan2['Kabupaten/Kota'] == kabterpilih) & (datapekerjaan2['Kecamatan'] == kecterpilih)]
    pekerjaan = pekerjaan2.groupby(['Kecamatan', 'Kelurahan/Desa', 'Pekerjaan'])['Jumlah Penduduk'].sum().reset_index()
    trimep8 = px.treemap(pekerjaan, path=['Kecamatan', 'Kelurahan/Desa', 'Pekerjaan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep8, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pekerjaan, hide_index=True, use_container_width=True)