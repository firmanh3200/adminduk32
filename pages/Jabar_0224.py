import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Adminduk Jabar', layout='wide')

with st.container(border=True):
    with st.container(border=True):
        st.title(':blue[Administrasi Kependudukan] :green[Jawa Barat] :orange[Semester 2 2024]')
        st.caption('Sumber: https://gis.dukcapil.kemendagri.go.id/peta/')

st.subheader('', divider='orange')

from data2 import datapenduduk
penduduk = datapenduduk.groupby(['Provinsi', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
keluarga = datapenduduk.groupby(['Provinsi', 'Kabupaten/Kota'])['Jumlah Kepala Keluarga'].sum().reset_index()

with st.container(border=True):
    st.subheader('Jumlah Penduduk')
    kol1a, kol1b = st.columns(2)
    with kol1a:
        with st.container(border=True):
            penduduk2 = penduduk.sort_values(by='Jumlah Penduduk', ascending=False)
            bar_penduduk = px.bar(penduduk2, x='Jumlah Penduduk', y='Kabupaten/Kota')
            st.plotly_chart(bar_penduduk, use_container_width=True)
    
    with kol1b:
        with st.container(border=True):
            pie_penduduk = px.pie(penduduk2, values='Jumlah Penduduk', color='Kabupaten/Kota')
            st.plotly_chart(pie_penduduk, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(penduduk2, hide_index=True, use_container_width=True)

st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader('Jumlah KK')
    kol2a, kol2b = st.columns(2)
    with kol2a:
        with st.container(border=True):
            keluarga2 = keluarga.sort_values(by='Jumlah Kepala Keluarga', ascending=False)
            bar_keluarga = px.bar(keluarga2, x='Jumlah Kepala Keluarga', y='Kabupaten/Kota')
            st.plotly_chart(bar_keluarga, use_container_width=True)
    
    with kol2b:
        with st.container(border=True):
            pie_keluarga = px.pie(keluarga2, values='Jumlah Kepala Keluarga', color='Kabupaten/Kota')
            st.plotly_chart(pie_keluarga, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(keluarga2, hide_index=True, use_container_width=True)
        
st.subheader('', divider='orange')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['Jenis Kelamin', 'Status Kawin', 'Agama', 
                                                          'Kelompok Umur', 'Pendidikan', 'Golongan Darah', 
                                                          'Usia Pendidikan', 'Pekerjaan'])

with tab1:
    from data2 import datajeniskelamin, datajeniskelamin2
    jeniskelamin = datajeniskelamin.groupby(['Provinsi', 'Kabupaten/Kota'])[['Laki-laki', 'Perempuan']].sum().reset_index()
    jeniskelamin2 = datajeniskelamin2.groupby(['Provinsi', 'Jenis Kelamin', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep1 = px.treemap(jeniskelamin2, path=['Provinsi', 'Jenis Kelamin', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep1, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(jeniskelamin, hide_index=True, use_container_width=True)

with tab2:
    from data2 import datastatuskawin2
    statuskawin = datastatuskawin2.groupby(['Provinsi', 'Status Kawin', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep2 = px.treemap(statuskawin, path=['Provinsi', 'Status Kawin', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep2, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(statuskawin, hide_index=True, use_container_width=True)
            
with tab3:
    from data2 import dataagama2
    agama = dataagama2.groupby(['Provinsi', 'Agama', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep3 = px.treemap(agama, path=['Provinsi', 'Agama', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep3, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(agama, hide_index=True, use_container_width=True)
            
with tab4:
    from data2 import dataumur2
    umur = dataumur2.groupby(['Provinsi', 'Kelompok Umur', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep4 = px.treemap(umur, path=['Provinsi', 'Kelompok Umur', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep4, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(umur, hide_index=True, use_container_width=True)
            
with tab5:
    from data2 import datapendidikan2
    pendidikan = datapendidikan2.groupby(['Provinsi', 'Pendidikan', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep5 = px.treemap(pendidikan, path=['Provinsi', 'Pendidikan', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep5, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pendidikan, hide_index=True, use_container_width=True)
            
with tab6:
    from data2 import datagolongandarah2
    goldar = datagolongandarah2.groupby(['Provinsi', 'Golongan Darah', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep6 = px.treemap(goldar, path=['Provinsi', 'Golongan Darah', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep6, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(goldar, hide_index=True, use_container_width=True)
            
with tab7:
    from data2 import datausiadidik2
    usia = datausiadidik2.groupby(['Provinsi', 'Usia Pendidikan', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep7 = px.treemap(usia, path=['Provinsi', 'Usia Pendidikan', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep7, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(usia, hide_index=True, use_container_width=True)
            
with tab8:
    from data2 import datapekerjaan2
    pekerjaan = datapekerjaan2.groupby(['Provinsi', 'Pekerjaan', 'Kabupaten/Kota'])['Jumlah Penduduk'].sum().reset_index()
    trimep8 = px.treemap(pekerjaan, path=['Provinsi', 'Pekerjaan', 'Kabupaten/Kota'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep8, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pekerjaan, hide_index=True, use_container_width=True)
            

st.subheader("", divider='orange')
st.caption('Tim Pembina Desa/ Kelurahan Cinta Statistik')