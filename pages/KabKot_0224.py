import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Adminduk Jabar', layout='wide')

with st.container(border=True):
    with st.container(border=True):
        st.title(':blue[Administrasi Kependudukan] :green[Jawa Barat] :orange[Semester 2 2024]')
        st.caption('Sumber: https://gis.dukcapil.kemendagri.go.id/peta/')

st.subheader('', divider='orange')

from data2 import pilihankab
kabterpilih = st.selectbox('Pilih Wilayah', pilihankab)

from data2 import datapenduduk
if kabterpilih:
    penduduk = datapenduduk[datapenduduk['Kabupaten/Kota'] == kabterpilih]
    penduduk2 = penduduk.groupby(['Kabupaten/Kota', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    keluarga = penduduk.groupby(['Kabupaten/Kota', 'Kecamatan'])['Jumlah Kepala Keluarga'].sum().reset_index()

with st.container(border=True):
    st.subheader(f'Jumlah Penduduk {kabterpilih}')
    kol1a, kol1b = st.columns(2)
    with kol1a:
        with st.container(border=True):
            penduduk3 = penduduk2.sort_values(by='Jumlah Penduduk', ascending=False)
            bar_penduduk = px.bar(penduduk3, x='Jumlah Penduduk', y='Kecamatan')
            st.plotly_chart(bar_penduduk, use_container_width=True)
    
    with kol1b:
        with st.container(border=True):
            pie_penduduk = px.pie(penduduk3, values='Jumlah Penduduk', color='Kecamatan')
            st.plotly_chart(pie_penduduk, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(penduduk3, hide_index=True, use_container_width=True)

st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader(f'Jumlah KK {kabterpilih}')
    kol2a, kol2b = st.columns(2)
    with kol2a:
        with st.container(border=True):
            keluarga2 = keluarga.sort_values(by='Jumlah Kepala Keluarga', ascending=False)
            bar_keluarga = px.bar(keluarga2, x='Jumlah Kepala Keluarga', y='Kecamatan')
            st.plotly_chart(bar_keluarga, use_container_width=True)
    
    with kol2b:
        with st.container(border=True):
            pie_keluarga = px.pie(keluarga2, values='Jumlah Kepala Keluarga', color='Kecamatan')
            st.plotly_chart(pie_keluarga, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(keluarga2, hide_index=True, use_container_width=True)
        
st.subheader('', divider='orange')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['Jenis Kelamin', 'Status Kawin', 'Agama', 
                                                          'Kelompok Umur', 'Pendidikan', 'Golongan Darah', 
                                                          'Usia Pendidikan', 'Pekerjaan'])

with tab1:
    from data2 import datajeniskelamin2
    jeniskelamin2 = datajeniskelamin2[datajeniskelamin2['Kabupaten/Kota'] == kabterpilih]
    jeniskelamin3 = jeniskelamin2.groupby(['Kabupaten/Kota', 'Jenis Kelamin', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep1 = px.treemap(jeniskelamin3, path=['Kabupaten/Kota', 'Jenis Kelamin', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep1, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(jeniskelamin3, hide_index=True, use_container_width=True)

with tab2:
    from data2 import datastatuskawin2
    statuskawin2 = datastatuskawin2[datastatuskawin2['Kabupaten/Kota'] == kabterpilih]
    statuskawin = statuskawin2.groupby(['Kabupaten/Kota', 'Status Kawin', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep2 = px.treemap(statuskawin, path=['Kabupaten/Kota', 'Status Kawin', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep2, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(statuskawin, hide_index=True, use_container_width=True)
            
with tab3:
    from data2 import dataagama2
    agama2 = dataagama2[dataagama2['Kabupaten/Kota'] == kabterpilih]
    agama = agama2.groupby(['Kabupaten/Kota', 'Agama', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep3 = px.treemap(agama, path=['Kabupaten/Kota', 'Agama', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep3, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(agama, hide_index=True, use_container_width=True)
            
with tab4:
    from data2 import dataumur2
    umur2 = dataumur2[dataumur2['Kabupaten/Kota'] == kabterpilih]
    umur = umur2.groupby(['Kabupaten/Kota', 'Kelompok Umur', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep4 = px.treemap(umur, path=['Kabupaten/Kota', 'Kelompok Umur', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep4, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(umur, hide_index=True, use_container_width=True)
            
with tab5:
    from data2 import datapendidikan2
    pendidikan2 = datapendidikan2[datapendidikan2['Kabupaten/Kota'] == kabterpilih]
    pendidikan = pendidikan2.groupby(['Kabupaten/Kota', 'Pendidikan', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep5 = px.treemap(pendidikan, path=['Kabupaten/Kota', 'Pendidikan', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep5, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pendidikan, hide_index=True, use_container_width=True)
            
with tab6:
    from data2 import datagolongandarah2
    goldar2 = datagolongandarah2[datagolongandarah2['Kabupaten/Kota'] == kabterpilih]
    goldar = goldar2.groupby(['Kabupaten/Kota', 'Golongan Darah', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep6 = px.treemap(goldar, path=['Kabupaten/Kota', 'Golongan Darah', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep6, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(goldar, hide_index=True, use_container_width=True)
            
with tab7:
    from data2 import datausiadidik2
    usia2 = datausiadidik2[datausiadidik2['Kabupaten/Kota'] == kabterpilih]
    usia = usia2.groupby(['Kabupaten/Kota', 'Usia Pendidikan', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep7 = px.treemap(usia, path=['Kabupaten/Kota', 'Usia Pendidikan', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep7, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(usia, hide_index=True, use_container_width=True)
            
with tab8:
    from data2 import datapekerjaan2
    pekerjaan2 = datapekerjaan2[datapekerjaan2['Kabupaten/Kota'] == kabterpilih]
    pekerjaan = pekerjaan2.groupby(['Kabupaten/Kota', 'Pekerjaan', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
    trimep8 = px.treemap(pekerjaan, path=['Kabupaten/Kota', 'Pekerjaan', 'Kecamatan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep8, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pekerjaan, hide_index=True, use_container_width=True)
            

st.subheader("", divider='orange')
st.caption('Tim Pembina Desa/ Kelurahan Cinta Statistik')