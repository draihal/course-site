import Link from 'next/link';

const HomeSection = props => (
    <div id='home'>
        {/* <!-- Start Landing Page Section --> */}
        <div className='landing'>
            <div className='home-wrap'>
                <div className='home-inner'>
                </div>
            </div>
        </div>
        <div className='caption text-center'>
            <div className='container'>
                <h1>{props.title}</h1>
                <h3>{props.short_description}</h3>
                <Link href='/'>
                    <a className='btn btn-outline-light btn-lg'>Выбрать</a>
                </Link>
            </div>
        </div>
        {/* <!-- End Landing Page Section --> */}
    </div>
);

export default HomeSection;
