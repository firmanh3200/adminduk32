const csvUrl = 'https://raw.githubusercontent.com/firmanh3200/adminduk32/main/gis-dukcapil.csv';
let parsedData;

Papa.parse(csvUrl, {
    download: true,
    header: true,
    complete: function(results) {
        parsedData = results.data;
        populateKabupaten();
    },
    error: function(error) {
        console.error("Error:", error);
    }
});

function populateKabupaten() {
    const kabupatenSelect = document.getElementById('kabterpilih');
    const kabupatenOptions = [...new Set(parsedData.map(item => item['Kabupaten/Kota']))];

    kabupatenOptions.forEach(kabupaten => {
        const option = document.createElement('option');
        option.value = kabupaten;
        option.textContent = kabupaten;
        kabupatenSelect.appendChild(option);
    });
}

function updateKecamatan() {
    const kabupatenSelect = document.getElementById('kabterpilih');
    const kecamatanSelect = document.getElementById('kecterpilih');
    const selectedKabupaten = kabupatenSelect.value;

    kecamatanSelect.innerHTML = '<option value="" selected disabled>Pilih Kecamatan</option>';

    const filteredData = parsedData.filter(item => item['Kabupaten/Kota'] === selectedKabupaten);
    const kecamatanOptions = [...new Set(filteredData.map(item => item['Kecamatan']))];

    kecamatanOptions.forEach(kecamatan => {
        const option = document.createElement('option');
        option.value = kecamatan;
        option.textContent = kecamatan;
        kecamatanSelect.appendChild(option);
    });
}

function updateDesa() {
    const kabupatenSelect = document.getElementById('kabterpilih');
    const kecamatanSelect = document.getElementById('kecterpilih');
    const desaSelect = document.getElementById('desaterpilih');
    const selectedKabupaten = kabupatenSelect.value;
    const selectedKecamatan = kecamatanSelect.value;

    desaSelect.innerHTML = '<option value="" selected disabled>Pilih Desa</option>';

    const filteredData = parsedData.filter(item =>
        item['Kabupaten/Kota'] === selectedKabupaten && item['Kecamatan'] === selectedKecamatan
    );
    const desaOptions = [...new Set(filteredData.map(item => item['Kelurahan/Desa']))];

    desaOptions.forEach(desa => {
        const option = document.createElement('option');
        option.value = desa;
        option.textContent = desa;
        desaSelect.appendChild(option);
    });
}

function updateDashboard() {
    const kabupatenSelect = document.getElementById('kabterpilih');
    const kecamatanSelect = document.getElementById('kecterpilih');
    const desaSelect = document.getElementById('desaterpilih');
    const selectedKabupaten = kabupatenSelect.value;
    const selectedKecamatan = kecamatanSelect.value;
    const selectedDesa = desaSelect.value;

    document.getElementById('desa-name').textContent = selectedDesa;
    document.getElementById('kecamatan-name').textContent = selectedKecamatan;
    document.getElementById('kabupaten-name').textContent = selectedKabupaten;

    const filteredData = parsedData.filter(item =>
        item['Kabupaten/Kota'] === selectedKabupaten &&
        item['Kecamatan'] === selectedKecamatan &&
        item['Kelurahan/Desa'] === selectedDesa
    )[0];

    document.getElementById('total-penduduk').textContent = filteredData['Jumlah Penduduk'];
    document.getElementById('laki-laki').textContent = filteredData['Laki-laki'];
    document.getElementById('perempuan').textContent = filteredData['Perempuan'];
    document.getElementById('jumlah-keluarga').textContent = filteredData['Jumlah Kepala Keluarga'];

    //Data jenis kelamin
    const jkData = [
        {JenisKelamin: 'Laki-laki', JumlahPenduduk: parseInt(filteredData['Laki-laki'])},
        {JenisKelamin: 'Perempuan', JumlahPenduduk: parseInt(filteredData['Perempuan'])}
    ];

    //Diagram Batang jenis kelamin
    const barJkOptions = {
        chart: {
            type: 'bar',
            height: '350',
            width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: jkData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: jkData.map(item => item.JenisKelamin)
        },
        title: {
            text: 'Jenis Kelamin',
            align: 'left'
        },
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const barJkChart = new ApexCharts(document.querySelector("#bar-jk"), barJkOptions);
    barJkChart.render();

    //Diagram Pie Jenis kelamin
    const pieKeluargaOptions = {
        chart: {
            type: 'pie',
            width: '100%',
            toolbar: { show: false }
        },
        series: jkData.map(item => item.JumlahPenduduk),
        labels: jkData.map(item => item.JenisKelamin),
        title: {
            text: 'Jenis Kelamin',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pieKeluargaChart = new ApexCharts(document.querySelector("#pie-keluarga"), pieKeluargaOptions);
    pieKeluargaChart.render();

    //Status Kawin
    const statusKawinData = [
        {statuskawin: 'Belum Kawin', JumlahPenduduk: parseInt(filteredData['Belum Kawin'])},
        {statuskawin: 'Kawin', JumlahPenduduk: parseInt(filteredData['Kawin'])},
        {statuskawin: 'Cerai Hidup', JumlahPenduduk: parseInt(filteredData['Cerai Hidup'])},
        {statuskawin: 'Cerai Mati', JumlahPenduduk: parseInt(filteredData['Cerai Mati'])}
    ];

    //trimep
	 const trimep2Options = {
        chart: {
            type: 'treemap',
            width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: statusKawinData.map(item => ({
                x: item.statuskawin,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Status Kawin',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep2Chart = new ApexCharts(document.querySelector("#trimep2"), trimep2Options);
    trimep2Chart.render();
	 //pie
     const pie2Options = {
        chart: {
            type: 'pie',
			width: '100%',
            toolbar: { show: false }
        },
        series: statusKawinData.map(item => item.JumlahPenduduk),
        labels: statusKawinData.map(item => item.statuskawin),
        title: {
            text: 'Status Kawin',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pie2Chart = new ApexCharts(document.querySelector("#pie2"), pie2Options);
    pie2Chart.render();
	//bar
    const bar2Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: statusKawinData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: statusKawinData.map(item => item.statuskawin)
        },
        title: {
            text: 'Status Kawin',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar2Chart = new ApexCharts(document.querySelector("#bar2"), bar2Options);
    bar2Chart.render();
	//Agama
    const agamaData = [
        {agama: 'Islam', JumlahPenduduk: parseInt(filteredData['Islam'])},
        {agama: 'Kristen', JumlahPenduduk: parseInt(filteredData['Kristen'])},
        {agama: 'Katholik', JumlahPenduduk: parseInt(filteredData['Katholik'])},
        {agama: 'Hindu', JumlahPenduduk: parseInt(filteredData['Hindu'])},
        {agama: 'Buddha', JumlahPenduduk: parseInt(filteredData['Buddha'])},
        {agama: 'Konghuchu', JumlahPenduduk: parseInt(filteredData['Konghuchu'])},
        {agama: 'Kepercayaan terhadap Tuhan YME', JumlahPenduduk: parseInt(filteredData['Kepercayaan terhadap Tuhan YME'])}
    ];
	//trimep
	     const trimep3Options = {
        chart: {
            type: 'treemap',
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: agamaData.map(item => ({
                x: item.agama,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Agama',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep3Chart = new ApexCharts(document.querySelector("#trimep3"), trimep3Options);
    trimep3Chart.render();

     //pie
	 const pie3Options = {
        chart: {
            type: 'pie',
			width: '100%',
            toolbar: { show: false }
        },
        series: agamaData.map(item => item.JumlahPenduduk),
        labels: agamaData.map(item => item.agama),
        title: {
            text: 'Agama',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pie3Chart = new ApexCharts(document.querySelector("#pie3"), pie3Options);
    pie3Chart.render();

	//bar
	 const bar3Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: agamaData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: agamaData.map(item => item.agama)
        },
        title: {
            text: 'Agama',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar3Chart = new ApexCharts(document.querySelector("#bar3"), bar3Options);
    bar3Chart.render();
		 //Kelompok Umur
     const kelompokUmurData = [
        {kelompokUmur: '00 - 04', JumlahPenduduk: parseInt(filteredData['00 - 04'])},
        {kelompokUmur: '05 - 09', JumlahPenduduk: parseInt(filteredData['05 - 09'])},
        {kelompokUmur: '10 - 14', JumlahPenduduk: parseInt(filteredData['10 - 14'])},
        {kelompokUmur: '15 - 19', JumlahPenduduk: parseInt(filteredData['15 - 19'])},
        {kelompokUmur: '20 - 24', JumlahPenduduk: parseInt(filteredData['20 - 24'])},
        {kelompokUmur: '25 - 29', JumlahPenduduk: parseInt(filteredData['25 - 29'])},
        {kelompokUmur: '30 - 34', JumlahPenduduk: parseInt(filteredData['30 - 34'])},
        {kelompokUmur: '35 - 39', JumlahPenduduk: parseInt(filteredData['35 - 39'])},
        {kelompokUmur: '40 - 44', JumlahPenduduk: parseInt(filteredData['40 - 44'])},
        {kelompokUmur: '45 - 49', JumlahPenduduk: parseInt(filteredData['45 - 49'])},
        {kelompokUmur: '50 - 54', JumlahPenduduk: parseInt(filteredData['50 - 54'])},
        {kelompokUmur: '55 - 59', JumlahPenduduk: parseInt(filteredData['55 - 59'])},
        {kelompokUmur: '60 - 64', JumlahPenduduk: parseInt(filteredData['60 - 64'])},
        {kelompokUmur: '65 - 69', JumlahPenduduk: parseInt(filteredData['65 - 69'])},
        {kelompokUmur: '70 - 74', JumlahPenduduk: parseInt(filteredData['70 - 74'])},
        {kelompokUmur: '75+', JumlahPenduduk: parseInt(filteredData['75+'])}
    ];
	// trimep
	 const trimep4Options = {
        chart: {
            type: 'treemap',
            width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: kelompokUmurData.map(item => ({
                x: item.kelompokUmur,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Kelompok Umur',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep4Chart = new ApexCharts(document.querySelector("#trimep4"), trimep4Options);
    trimep4Chart.render();
		 //pie
     const pie4Options = {
        chart: {
            type: 'pie',
			width: '100%',
            toolbar: { show: false }
        },
        series: kelompokUmurData.map(item => item.JumlahPenduduk),
        labels: kelompokUmurData.map(item => item.kelompokUmur),
        title: {
            text: 'Kelompok Umur',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pie4Chart = new ApexCharts(document.querySelector("#pie4"), pie4Options);
    pie4Chart.render();

		//bar
	 const bar4Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: kelompokUmurData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: kelompokUmurData.map(item => item.kelompokUmur)
        },
        title: {
            text: 'Kelompok Umur',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar4Chart = new ApexCharts(document.querySelector("#bar4"), bar4Options);
    bar4Chart.render();
			//Pendidikan
     const pendidikanData = [
        {pendidikan: 'Tidak/Belum Sekolah', JumlahPenduduk: parseInt(filteredData['Tidak/Belum Sekolah'])},
        {pendidikan: 'Belum Tamat SD', JumlahPenduduk: parseInt(filteredData['Belum Tamat SD'])},
        {pendidikan: 'Tamat SD', JumlahPenduduk: parseInt(filteredData['Tamat SD'])},
        {pendidikan: 'SLTP', JumlahPenduduk: parseInt(filteredData['SLTP'])},
        {pendidikan: 'SLTA', JumlahPenduduk: parseInt(filteredData['SLTA'])},
        {pendidikan: 'D1 dan D2', JumlahPenduduk: parseInt(filteredData['D1 dan D2'])},
        {pendidikan: 'D3', JumlahPenduduk: parseInt(filteredData['D3'])},
        {pendidikan: 'S1', JumlahPenduduk: parseInt(filteredData['S1'])},
        {pendidikan: 'S2', JumlahPenduduk: parseInt(filteredData['S2'])},
        {pendidikan: 'S3', JumlahPenduduk: parseInt(filteredData['S3'])}
    ];
		//trimep
		  const trimep5Options = {
        chart: {
            type: 'treemap',
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: pendidikanData.map(item => ({
                x: item.pendidikan,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Pendidikan',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep5Chart = new ApexCharts(document.querySelector("#trimep5"), trimep5Options);
    trimep5Chart.render();

	//pie
	 const pie5Options = {
        chart: {
            type: 'pie',
			width: '100%',
            toolbar: { show: false }
        },
        series: pendidikanData.map(item => item.JumlahPenduduk),
        labels: pendidikanData.map(item => item.pendidikan),
        title: {
            text: 'Pendidikan',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pie5Chart = new ApexCharts(document.querySelector("#pie5"), pie5Options);
    pie5Chart.render();
 //bar
    const bar5Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: pendidikanData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: pendidikanData.map(item => item.pendidikan)
        },
        title: {
            text: 'Pendidikan',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar5Chart = new ApexCharts(document.querySelector("#bar5"), bar5Options);
    bar5Chart.render();
  //Golongan Darah
     const goldarData = [
        {goldar: 'O', JumlahPenduduk: parseInt(filteredData['O'])},
        {goldar: 'B-', JumlahPenduduk: parseInt(filteredData['B-'])},
        {goldar: 'B+', JumlahPenduduk: parseInt(filteredData['B+'])},
        {goldar: 'O+', JumlahPenduduk: parseInt(filteredData['O+'])},
        {goldar: 'AB-', JumlahPenduduk: parseInt(filteredData['AB-'])},
        {goldar: 'A', JumlahPenduduk: parseInt(filteredData['A'])},
        {goldar: 'Tidak Diketahui', JumlahPenduduk: parseInt(filteredData['Tidak Diketahui'])},
        {goldar: 'AB+', JumlahPenduduk: parseInt(filteredData['AB+'])},
        {goldar: 'A+', JumlahPenduduk: parseInt(filteredData['A+'])},
        {goldar: 'A-', JumlahPenduduk: parseInt(filteredData['A-'])},
        {goldar: 'O-', JumlahPenduduk: parseInt(filteredData['O-'])},
        {goldar: 'B', JumlahPenduduk: parseInt(filteredData['B'])},
        {goldar: 'AB', JumlahPenduduk: parseInt(filteredData['AB'])}
    ];
		  //trimep
		   const trimep6Options = {
        chart: {
            type: 'treemap',
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: goldarData.map(item => ({
                x: item.goldar,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Golongan Darah',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep6Chart = new ApexCharts(document.querySelector("#trimep6"), trimep6Options);
    trimep6Chart.render();
		//pie
		 const pie6Options = {
        chart: {
            type: 'pie',
			width: '100%',
            toolbar: { show: false }
        },
        series: goldarData.map(item => item.JumlahPenduduk),
        labels: goldarData.map(item => item.goldar),
        title: {
            text: 'Golongan Darah',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
       responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pie6Chart = new ApexCharts(document.querySelector("#pie6"), pie6Options);
    pie6Chart.render();
		//bar
		 const bar6Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: goldarData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: goldarData.map(item => item.goldar)
        },
        title: {
            text: 'Golongan Darah',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar6Chart = new ApexCharts(document.querySelector("#bar6"), bar6Options);
    bar6Chart.render();
 //Usia Pendidikan
     const usiaPendidikanData = [
        {usiaPendidikan: '03 - 04', JumlahPenduduk: parseInt(filteredData['03 - 04'])},
        {usiaPendidikan: '05', JumlahPenduduk: parseInt(filteredData['05'])},
        {usiaPendidikan: '06 - 11', JumlahPenduduk: parseInt(filteredData['06 - 11'])},
        {usiaPendidikan: '12 - 14', JumlahPenduduk: parseInt(filteredData['12 - 14'])},
        {usiaPendidikan: '15 - 17', JumlahPenduduk: parseInt(filteredData['15 - 17'])},
        {usiaPendidikan: '18 - 22', JumlahPenduduk: parseInt(filteredData['18 - 22'])}
    ];
	//trimep
		  const trimep7Options = {
        chart: {
            type: 'treemap',
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: usiaPendidikanData.map(item => ({
                x: item.usiaPendidikan,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Usia Pendidikan',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep7Chart = new ApexCharts(document.querySelector("#trimep7"), trimep7Options);
    trimep7Chart.render();
	//pie
	const pie7Options = {
        chart: {
            type: 'pie',
			width: '100%',
            toolbar: { show: false }
        },
        series: usiaPendidikanData.map(item => item.JumlahPenduduk),
        labels: usiaPendidikanData.map(item => item.usiaPendidikan),
        title: {
            text: 'Usia Pendidikan',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const pie7Chart = new ApexCharts(document.querySelector("#pie7"), pie7Options);
    pie7Chart.render();
	//bar
    const bar7Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: usiaPendidikanData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: usiaPendidikanData.map(item => item.usiaPendidikan)
        },
        title: {
            text: 'Usia Pendidikan',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar7Chart = new ApexCharts(document.querySelector("#bar7"), bar7Options);
    bar7Chart.render();
	
	 //Pekerjaan
    const pekerjaanData = [
        {pekerjaan: 'Belum/Tidak Bekerja', JumlahPenduduk: parseInt(filteredData['Belum/Tidak Bekerja'] || 0)},
        {pekerjaan: 'Pensiunan', JumlahPenduduk: parseInt(filteredData['Pensiunan'] || 0)},
        {pekerjaan: 'Mengurus Rumah Tannga', JumlahPenduduk: parseInt(filteredData['Mengurus Rumah Tannga'] || 0)},
        {pekerjaan: 'Perdagangan', JumlahPenduduk: parseInt(filteredData['Perdagangan'] || 0)},
        {pekerjaan: 'Perawat', JumlahPenduduk: parseInt(filteredData['Perawat'] || 0)},
        {pekerjaan: 'Nelayan', JumlahPenduduk: parseInt(filteredData['Nelayan'] || 0)},
        {pekerjaan: 'Pelajar dan Mahasiswa', JumlahPenduduk: parseInt(filteredData['Pelajar dan Mahasiswa'] || 0)},
        {pekerjaan: 'Guru', JumlahPenduduk: parseInt(filteredData['Guru'] || 0)},
        {pekerjaan: 'Wiraswasta', JumlahPenduduk: parseInt(filteredData['Wiraswasta'] || 0)},
        {pekerjaan: 'Pengacara', JumlahPenduduk: parseInt(filteredData['Pengacara'] || 0)},
        {pekerjaan: 'Pekerjaan Lainnya', JumlahPenduduk: parseInt(filteredData['Pekerjaan Lainnya'] || 0)}
    ];

console.log("Data Pekerjaan:", pekerjaanData);
     //Pie (Ganti Treemap jika ada masalah)
    const pie8Options = {
        chart: {
            type: 'pie',
	    width: '100%',
            toolbar: { show: false }
        },
        series: pekerjaanData.map(item => item.JumlahPenduduk),
        labels: pekerjaanData.map(item => item.pekerjaan),
        title: {
            text: 'Pekerjaan',
            align: 'left'
        },
	legend: {
      		show: true,
		position: 'bottom'
	},
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: "100%"
                }
            }
        }]
    };

    const pie8Chart = new ApexCharts(document.querySelector("#pie8"), pie8Options);
    pie8Chart.render();

	//treemap
	 const trimep8Options = {
        chart: {
            type: 'treemap',
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: pekerjaanData.map(item => ({
                x: item.pekerjaan,
                y: item.JumlahPenduduk
            }))
        }],
        title: {
            text: 'Pekerjaan',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const trimep8Chart = new ApexCharts(document.querySelector("#trimep8"), trimep8Options);
    trimep8Chart.render();
	
	//bar
	const bar8Options = {
        chart: {
            type: 'bar',
            height: 350,
			width: '100%',
            toolbar: { show: false }
        },
        series: [{
            data: pekerjaanData.map(item => item.JumlahPenduduk)
        }],
        xaxis: {
            categories: pekerjaanData.map(item => item.pekerjaan)
        },
        title: {
            text: 'Pekerjaan',
            align: 'left'
        },
		responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const bar8Chart = new ApexCharts(document.querySelector("#bar8"), bar8Options);
    bar8Chart.render();

}
