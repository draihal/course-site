import Link from 'next/link';

const PartnersSection = () => (
    <div id='partners' className='offset'>
        <div className='container'>
            <div className='col-12 narrow text-center'>
                <h3 className='heading'>Ждут выпуска</h3>
            </div>
            <section className='customer-logos slider'>
                <div className='slide'><i className='fab fa-amazon fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-apple fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-cc-amex fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-tripadvisor fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-yandex fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-facebook fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-google fa-5x'> </i></div>
                <div className='slide'><i className='fab fa-odnoklassniki fa-5x'> </i></div>
            </section>
        </div>
    </div>
);

export default PartnersSection;
