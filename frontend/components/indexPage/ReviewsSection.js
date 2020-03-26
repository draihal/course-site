import Link from 'next/link';

function urlFor (source) {
    return (`${process.env.basePath}${source}`)
}

const ReviewsSection = props => (
    <div id='reviews' className='offset'>
        <div className='jumbotron'>
            <div className='container'>
                <div className='col-12 text-center'>
                    <h3 className='heading'>Отзывы</h3>
                    <div className='heading-underline'> </div>
                </div>
                <div className='row'>
                    {props.reviews.map(review => (
                        <div className='col-md-6 reviews' key={review.id}>
                            <div className='row'>
                                <div className='col-md-4'>
                                    {review.student_image ? <img src={urlFor(review.student_image)} /> : <img src='static/default_user.jpg' />}
                                </div>
                                <div className='col-md-8'>
                                    <blockquote>
                                        <i className='fas fa-quote-left'> </i>
                                        <i>{review.text}</i>
                                        <hr className='reviews-hr' />
                                        <cite>&#8212; {review.student_first_name} {review.student_last_name}</cite>
                                    </blockquote>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
        <div className='col-12 narrow text-center'>
            <p className='lead'>Хочешь узнать больше мнений?</p>
            <a className='btn btn-secondary btn-md' href='#'>Другие отзывы</a>
        </div>
    </div>
);

export default ReviewsSection;
