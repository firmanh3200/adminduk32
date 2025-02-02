import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Adminduk Jabar', layout='wide')

with st.container(border=True):
    with st.container(border=True):
        st.title(':blue[Administrasi Kependudukan] :green[Jawa Barat] :orange[Semester 1 2024]')
        st.caption('Sumber: https://gis.dukcapil.kemendagri.go.id/peta/')

st.subheader('', divider='orange')

from data import datapenduduk
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
    from data import datajeniskelamin, datajeniskelamin2
    jeniskelamin = datajeniskelamin.groupby(['Provinsi', 'Kabupaten/Kota'])[['Laki-laki', 'Perempuan']].sum().reset_index()
    jeniskelamin2 = datajeniskelamin2.groupby(['Provinsi', 'Kabupaten/Kota', 'Jenis Kelamin'])['Jumlah Penduduk'].sum().reset_index()
    trimep1 = px.treemap(jeniskelamin2, path=['Provinsi', 'Kabupaten/Kota', 'Jenis Kelamin'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep1, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(jeniskelamin, hide_index=True, use_container_width=True)

with tab2:
    from data import datastatuskawin2
    statuskawin = datastatuskawin2.groupby(['Provinsi', 'Kabupaten/Kota', 'Status Kawin'])['Jumlah Penduduk'].sum().reset_index()
    trimep2 = px.treemap(statuskawin, path=['Provinsi', 'Kabupaten/Kota', 'Status Kawin'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep2, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(statuskawin, hide_index=True, use_container_width=True)
            
with tab3:
    from data import dataagama2
    agama = dataagama2.groupby(['Provinsi', 'Kabupaten/Kota', 'Agama'])['Jumlah Penduduk'].sum().reset_index()
    trimep3 = px.treemap(agama, path=['Provinsi', 'Kabupaten/Kota', 'Agama'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep3, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(agama, hide_index=True, use_container_width=True)
            
with tab4:
    from data import dataumur2
    umur = dataumur2.groupby(['Provinsi', 'Kabupaten/Kota', 'Kelompok Umur'])['Jumlah Penduduk'].sum().reset_index()
    trimep4 = px.treemap(umur, path=['Provinsi', 'Kabupaten/Kota', 'Kelompok Umur'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep4, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(umur, hide_index=True, use_container_width=True)
            
with tab5:
    from data import datapendidikan2
    pendidikan = datapendidikan2.groupby(['Provinsi', 'Kabupaten/Kota', 'Pendidikan'])['Jumlah Penduduk'].sum().reset_index()
    trimep5 = px.treemap(pendidikan, path=['Provinsi', 'Kabupaten/Kota', 'Pendidikan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep5, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pendidikan, hide_index=True, use_container_width=True)
            
with tab6:
    from data import datagolongandarah2
    goldar = datagolongandarah2.groupby(['Provinsi', 'Kabupaten/Kota', 'Golongan Darah'])['Jumlah Penduduk'].sum().reset_index()
    trimep6 = px.treemap(goldar, path=['Provinsi', 'Kabupaten/Kota', 'Golongan Darah'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep6, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(goldar, hide_index=True, use_container_width=True)
            
with tab7:
    from data import datausiadidik2
    usia = datausiadidik2.groupby(['Provinsi', 'Kabupaten/Kota', 'Usia Pendidikan'])['Jumlah Penduduk'].sum().reset_index()
    trimep7 = px.treemap(usia, path=['Provinsi', 'Kabupaten/Kota', 'Usia Pendidikan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep7, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(usia, hide_index=True, use_container_width=True)
            
with tab8:
    from data import datapekerjaan2
    pekerjaan = datapekerjaan2.groupby(['Provinsi', 'Kabupaten/Kota', 'Pekerjaan'])['Jumlah Penduduk'].sum().reset_index()
    trimep8 = px.treemap(pekerjaan, path=['Provinsi', 'Kabupaten/Kota', 'Pekerjaan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep8, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pekerjaan, hide_index=True, use_container_width=True)