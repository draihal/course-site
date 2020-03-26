import Layout from '../components/Layout';
import HomeSection from '../components/indexPage/HomeSection';
import CoursesSection from '../components/indexPage/CoursesSection';
import TeacherSection from '../components/indexPage/TeacherSection';
import PartnersSection from '../components/indexPage/PartnersSection';
import ReviewsSection from '../components/indexPage/ReviewsSection';
import fetch from 'isomorphic-unfetch';
import axios from 'axios';
import {catchAxiosError} from '../services/error';


const Homepage = ({errorCode, indexPage}) => {
    if (errorCode) {
        return <Error statusCode={errorCode}/>
    }
    return <Layout>
        <HomeSection
            title={indexPage.title}
            short_description={indexPage.short_description}/>
        <CoursesSection
            description={indexPage.description}
            number_of_students={indexPage.number_of_students}
            number_of_groups={indexPage.number_of_groups}
            number_of_teachers={indexPage.number_of_teachers}/>
        <TeacherSection teachers={indexPage.random_three_teachers}/>
        {/*<PartnersSection/>  // TODO: add https://www.framer.com/api/motion/ */}
        <ReviewsSection reviews={indexPage.random_two_reviews}/>
    </Layout>
};

Homepage.getInitialProps = async function() {
    const res = await axios.get(`${process.env.basePath}/api/v1/pages/index/`);
    const errorCode = res.statusCode > 200 ? res.statusCode : false;
    const indexPage = res.data;
    return { errorCode, indexPage };
};

export default Homepage;

